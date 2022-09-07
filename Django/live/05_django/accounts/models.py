from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser): #기존 유저모델을 안쓰겠다.
    pass
