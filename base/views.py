from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer,CourseSerializer
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from base.models import User
from django.http import HttpResponseRedirect
from courses.models import Course
from rest_framework.generics import ListCreateAPIView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['is_tutor'] =user.is_staff
        token['is_admin']=user.is_superadmin
        # ...

        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)


class UserRegistration(APIView):
      def post(self, request, format=None):
          email = request.data.get('email')
          print(request.data)
        

          serializer = UserSerializer(data=request.data)
          #print(serializer.is_valid())
          if serializer.is_valid(raise_exception=True):
            
            user = serializer.save()
            
            current_site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            mail_subject = 'Please activate your account'
            
            message = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': 'https://eduhub-learn.netlify.app',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                'usename': urlsafe_base64_encode(force_bytes(user.username))
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            return Response({'msg':'Registration Success'})
            

          return Response({'msg':'Registration Failed'})
  

@api_view(['GET'])
def activate(request, uidb64, token):
    try:

        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk = uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        print('checked')
        user.is_active = True
        user.save()
      

        return HttpResponseRedirect('https://eduhub-learn.netlify.app/login')
    
class Listuser(ListCreateAPIView):
    queryset = User.objects.filter(is_admin=False)
    serializer_class = UserSerializer
    
    
class Blockuser(APIView):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        print(user.is_active)
        user.is_active = not user.is_active
        user.save()
        return Response({'msg': 200})
    

class Singleuser(APIView):
    def get(self, request, pk):
        query = Course.objects.get(id=pk)
        serializer = CourseSerializer(query)
        return Response(serializer.data)

    
class Singlecourse(APIView):
    def get(self, request, pk):
        query = Course.objects.get(id=pk)
        serializer = CourseSerializer(query)
        return Response(serializer.data) 
    

class GetProfile(APIView):
    def get(self, request, pk):
        user = User.objects.filter(id=pk)
        print(user)
        
        serializer = UserSerializer(user,many=True)
        
        return Response(serializer.data)


class ResetPassword(APIView):
    def post(self, request, format=None):
        
        str_user_id = request.data.get('user_id')
        user_id = int(str_user_id)
        password = request.data.get('password')
        
        print(user_id)
        if user_id :
            
            user = User.objects.get(pk=user_id)
            user.set_password(password)
            user.save()
            print('saved')

            return Response({'msg': 'Password Updated Successfully'})
    
        return HttpResponseRedirect('https://eduhub-learn.netlify.app/reset-password')
    
    
class ChangeImage(APIView):
    def post(self,request, format=None):
        print(request.data)
        current_user = request.data.get('user')
        user = User.objects.get(id=current_user)
        image = request.data.get('image')
        
        user.image = image
        user.save()
        
        return Response({'msg':200})
    
    
class UpdateProfile(APIView):
    def post(self, request, format=None):
        user_id = request.data['user_id']
        current_user = User.objects.get(id=user_id)
        current_user.first_name = request.data['first_name']
        current_user.last_name = request.data['last_name']
        current_user.phone_number = request.data['phone_number']
        current_user.save()
        return Response({'msg':200})
    

class ChangePass(APIView):
    def post(self, request, format=None):
        oldpassword = request.data['oldpass']
        password = request.data['password']
        user_id = request.data['user_id']
        
        user = User.objects.get(id=user_id)

        success = user.check_password(oldpassword)
        if success:
            user.set_password(password)
            user.save()
            print("updated")
            data = {
                'msg': 200
            }
            return Response(data)
        else:
            print("Not done")
            data = {
                'msg': 500
            }
            return Response(data)

    