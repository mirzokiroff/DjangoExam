from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    company = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(max_length=128, blank=True, null=True)
    # image = models.ImageField(upload_to='images', blank=True, null=True)
    image = models.ImageField(upload_to='pic/', blank=True, null=True, default='https://bootdey.com/img/Content/avatar/avatar1.png')
    created_at = models.DateTimeField(auto_now_add=True)

