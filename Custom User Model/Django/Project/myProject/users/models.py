from django.db import models                                        # HP 10 L3
from django.contrib.auth.models import AbstractUser                 # HP 10 L3

class CustomUser(AbstractUser):                                     # HP 10 L3
    sex_choice = ((0, "Nữ"), (1, "Nam"), (2, "Không xác định"))     # HP 10 L3
    age = models.IntegerField(default=0)                            # HP 10 L3
    sex = models.IntegerField(choices=sex_choice, default=0)        # HP 10 L3
    address = models.CharField(default="", max_length=255)          # HP 10 L3
