from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([AllowAny])
def ping(request):
    return Response({"message": "Auth service is running."})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def validate_permission(request):
    # Analyse permission
    required_permission = request.data.get('permission')
    user = request.user
    if user.has_perm(required_permission):
        return Response({'status': 'authorized'})
    else:
        return Response({'status': 'unauthorized'}, status=403)
    
# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = {
                "username": user.username,
                "email": user.email,
                "phone": getattr(user, 'phone', None),
            }
            return Response({
                "message": "User registered successfully",
                "data": data
            }, status=201)
        return Response({
            "message": "Registration failed",
            "errors": serializer.errors
        }, status=400)

from django.contrib.auth import authenticate
from .models import CustomUser

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({
                "message": "Login failed",
                "errors": {
                    "detail": "Invalid email or password"
                }
            }, status=400)

        user = authenticate(username=user.username, password=password)

        if not user:
            return Response({
                "message": "Login failed",
                "errors": {
                    "detail": "Invalid email or password"
                }
            }, status=400)

        token, created = Token.objects.get_or_create(user=user)
        return Response({
             "message": "Login successful",
             "data": {
                "token": token.key,
                "user_id": user.pk,
                "username": user.username,
                "email": user.email
            }
        })