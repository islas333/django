from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    foundation = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
      if not self.password.startswith('pbkdf2_sha256$'):
        self.password = make_password(self.password)
      super().save(*args, **kwargs)