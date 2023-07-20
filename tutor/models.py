from django.db import models
from base.models import User

# Create your models here.

class Tutor(models.Model):
    full_name=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    mobile_no=models.CharField(max_length=100,default='')
    skills=models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
  

    def __str__(self):
     if self.full_name:
        return self.full_name
   #   elif self.user:
   #      return self.user.username
     else:
        return "Tutor"
