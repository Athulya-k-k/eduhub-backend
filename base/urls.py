from django.urls import path
from . import views
from . views import MyTokenObtainPairView,UserRegistration,Listuser,Blockuser,GetProfile,UpdateProfile,ChangePass,ChangeImage

from rest_framework_simplejwt.views import (
  
    TokenRefreshView,
)


urlpatterns = [
    path('',views.getRoutes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',UserRegistration.as_view()),
    path('activate/<uidb64>/<token>',views.activate, name='activate'),
    path('users/', Listuser.as_view(),name='users'),
    path('blockuser/<int:pk>',Blockuser.as_view(),name='blockuser'),
    path('profile/<int:pk>',GetProfile.as_view(),name='profile'),
    path('updateprofile/',UpdateProfile.as_view(),name='updateprofile'),
    path('changepass/',ChangePass.as_view(),name='changepass'),
    path('updateimage/',ChangeImage.as_view(),name='updateimage'),
    
]

