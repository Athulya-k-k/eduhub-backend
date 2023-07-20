from django.urls import path
from . import views
from .views import Cours,Categor, DeleteView,CreateCourse,BlockCourse,RejectCourse,CreateCategory,ApproveCourse,CategoryDeleteView
from base.views import Singlecourse,Singleuser
from courses.views import HomeListCourse,MyCourses

urlpatterns = [
    path('course/', Cours.as_view(), name='course'),
    path('delete-course/<int:course_id>', views.CourseDeleteView.as_view(), name='course-delete'),
    path('category/', Categor.as_view(), name='category'),
    path('delete-category/<int:cat_id>/', CategoryDeleteView.as_view(), name='delete-category'),
    path('singlecourse/<int:pk>', Singlecourse.as_view(), name='singlecourse'),
    path('singleuser/<int:pk>', Singleuser.as_view(), name='singleuser'),
    path('homelistcourse/', HomeListCourse.as_view(), name='homelistcourse'),
    path('update-course/<int:course_id>', views.CourseUpdateView.as_view()),
    path('update-category/<int:cat_id>', views.CategoryUpdateView.as_view()),
    path('createcourse/', CreateCourse.as_view()),
    path('createcourse/<int:course_id>', CreateCourse.as_view()),
    path('createcategory/', CreateCategory.as_view()),
    path('createcategory/<int:cat_id>', CreateCategory.as_view()),
    path('blockcourse/<int:pk>', BlockCourse.as_view()),
    path('approvecourse/<int:user_id>/<int:pk>', ApproveCourse.as_view()), 
     path('mycourse/<int:pk>',MyCourses.as_view(),name='mycourse'),  
]