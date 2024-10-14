from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    sex_choice = ((0, "Nữ"), (1, "Nam"), (2, "Không xác định"))
    age = models.IntegerField(default=0)
    sex = models.IntegerField(choices=sex_choice, default=0)
    address = models.CharField(default="", max_length=255)
