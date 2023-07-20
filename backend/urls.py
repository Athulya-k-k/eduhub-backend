from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from courses.views import CourseDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('base.urls')),
    path('api-tutor/',include('tutor.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('courses/',include('courses.urls')),
    path('payment/', include("payment.urls")),
    path('msg/',include('message.urls')),
    path('learning/',include('learning.urls')),
    path('cart/',include('cart.urls')),
    path('csession/',include('csession.urls')),

 
  
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)