from django.db import models
from base.models import User
from tutor.models import Tutor
from payment.models import Order
# from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/categ')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    title = models.CharField(max_length=500, null=False)
    description = models.CharField(max_length=600, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/course')
    video = models.FileField(upload_to='photos/course')
    is_active = models.BooleanField(default=False)
    price = models.IntegerField()
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    
    # class Meta:
    #     ordering = ['-created_at']



class EnrolledCourse(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    courseprogress = models.CharField(max_length=100)



