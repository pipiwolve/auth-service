from django.urls import path
from .views import RegisterView, CustomAuthToken, validate_permission, ping, list_users, delete_user

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('permission/', validate_permission, name='validate_permission'),
    path('ping/', ping, name='ping'), 
    path('users/', list_users, name='list_users'),
    path('users/<int:user_id>/', delete_user, name='delete_user'),
]