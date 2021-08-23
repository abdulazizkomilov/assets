from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    tel = models.PositiveIntegerField()
    text = models.CharField(max_length=250)
    subject = models.TextField()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('home')