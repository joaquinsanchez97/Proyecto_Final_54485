from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #SubCarpeta de avatares
    image = models.ImageField(upload_to="avatares", null = True, blank = True)