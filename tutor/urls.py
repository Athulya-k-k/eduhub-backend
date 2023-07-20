from django.urls import path
from . import views
# from .views import Tutorregister 
from . views import TeacherList, TutorLogin
from .models import Tutor
from .views import BlockTutorView,UnblockTutorView


urlpatterns = [
    path('tutor/', views.TeacherList.as_view()),
    path('tutor/<int:pk>/', views.TeacherDetail.as_view()),
    path('teacherlogin/', views.TutorLogin.as_view()),
    path('block/<int:tutor_id>/', BlockTutorView.as_view(), name='block_tutor'),
    path('tutor/unblock/<int:tutor_id>/', UnblockTutorView.as_view(), name='unblock_tutor'),
]