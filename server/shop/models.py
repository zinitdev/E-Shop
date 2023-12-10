from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(
        upload_to="uploads/%Y/%m/%d",
        default=None,
        null=True,
        blank=True,
        help_text="Upload avatar of the user.",
    )

    def __str__(self):
        return self.username