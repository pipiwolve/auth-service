from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def validate_permission(request):
    # 解析请求中的权限参数（如所需权限或角色）
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

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })