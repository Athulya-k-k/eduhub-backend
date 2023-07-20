from django.db import models
from base.models import User
from courses.models import EnrolledCourse,Course
from csession.models import Lecture
# Create your models here.


class Progress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture,on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    current_course = models.ForeignKey(EnrolledCourse,on_delete=models.CASCADE)
    
    
    
class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    rating = models.CharField(max_length=10,null=True)
    discription = models.CharField(max_length=800,null=False)