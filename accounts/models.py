from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    # 其他自定义字段

# settings.py 中指定自定义用户模型
AUTH_USER_MODEL = 'accounts.CustomUser'