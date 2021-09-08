from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User


class extendedUser(models.Model):
    
    register=models.CharField(max_length=30)
    user=models.OneToOneField(User,on_delete=models.CASCADE)