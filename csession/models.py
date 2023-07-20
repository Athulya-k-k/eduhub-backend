from django.db import models
from courses.models import Course

# Create your models here.


class Sessions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=800)
    description = models.CharField(max_length=800)


    
class Lecture(models.Model):
    session = models.ForeignKey(Sessions, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=600)
    description = models.CharField(max_length=600)
    type = models.CharField(max_length=100)
    material = models.FileField(upload_to='photos/course',null=True)