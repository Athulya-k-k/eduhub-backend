from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import ProgressView,AddReview,GetReview,UpdateProgress,GetProgress


urlpatterns = [
    path('progress/<int:pk>/<int:id>',ProgressView.as_view(), name='progress'),
    path('addreview/',AddReview.as_view(),name='addreview'),
    path('getreview/<int:pk>',GetReview.as_view(),name='getreview'),
    path('progressupdate/<int:pk>/<int:id>',UpdateProgress.as_view(),name='progressupdate'),
    path('getprogress/<int:pk>/<int:id>',GetProgress.as_view(), name='getprogress'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)