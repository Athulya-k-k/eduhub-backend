from django.urls import path
from . import views
# from .views import Tutorregister 
from .models import Tutor



urlpatterns = [
    path('send-message/<int:tutor_id>/<int:user_id>',views.save_teacher_student_msg),
  
]