from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    password = None

    def __str__(self) -> str:
        return (f"user's phone number: {self.username}")
