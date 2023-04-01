from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField()
    first_name = models.TextField(max_length=25)
    last_name = models.TextField(max_length=35)