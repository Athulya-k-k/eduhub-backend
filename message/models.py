from django.db import models
from tutor.models import Tutor
from base.models import User

# Create your models here.

class TeacherStudentChat(models.Model):
    teacher=models.ForeignKey(Tutor,on_delete=models.CASCADE)
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    msg_text=models.TextField()
    msg_from=models.CharField(max_length=100)
    msg_time=models.DateTimeField(auto_now_add=True)