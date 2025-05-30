from django.urls import path
from .views import RegisterView, CustomAuthToken, validate_permission, ping

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('permission/', validate_permission, name='validate_permission'),
    path('ping/', ping, name='ping'), 
]