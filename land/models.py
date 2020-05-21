from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Product(models.Model):

    title = models.CharField(
        max_length=16,
    )

    image = models.ImageField()

    price = models.CharField(
        max_length=64,
        default="$9.95"
    )

    def __str__(self):
        return self.title
