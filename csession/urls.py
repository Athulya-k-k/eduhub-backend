from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import SessionView,LectureView,AddSession,AddMaterial


urlpatterns = [
    path('session/<int:pk>', SessionView.as_view(), name='session'),
    path('lectures/<int:pk>',LectureView.as_view(), name='lectures'),
    path('addsession/',AddSession.as_view(), name='addsession'),
    path('addmaterial/',AddMaterial.as_view(), name='addmaterial')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)