from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
   
    
    USERNAME_FIELD = 'email' # overiding username for the email field.
    
    REQUIRED_FIELDS = []
