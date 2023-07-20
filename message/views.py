from django.shortcuts import render
from tutor.models import Tutor
from base.models import User
from .models import TeacherStudentChat
from . import models
from django.http import JsonResponse

# Create your views here.
def save_teacher_student_msg(request,tutor_id,user_id):
    tutor=Tutor.objects.get(id=tutor_id)
    user=User.objects.get(id=user_id)
    msg_text=request.POST.get('msg_text')
    msg_from=request.POST.get('msg_from')
    msgRes=models.TeacherStudentChat.objects.create(

    )
    if msgRes:
        return JsonResponse({'bool':True,'msg':'msg dend'})
    else:
        return JsonResponse({'bool':False,'msg':'msg:error'})

