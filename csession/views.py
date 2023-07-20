from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from .models import Sessions,Lecture
from base.models import User
from courses.models import Course,EnrolledCourse
from .serializers import SessionsSerializer,LectureSerializer,CourseSerializer

from payment.serializers import EnrolledSerializer




from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
# Create your views here.


class SessionView(APIView):
    def get(self, request, pk):
        print(pk)
        queryset = Sessions.objects.filter(course=pk)
        serializer = SessionsSerializer(queryset, many=True)
        
        return Response(serializer.data)
    
class LectureView(APIView):
    def get(self, request, pk):
        queryset = Lecture.objects.filter(course=pk)
        serializer = LectureSerializer(queryset, many=True)
        
        return Response(serializer.data)

        
class AddSession(APIView):
    def post(self, request, format=None):
        session = SessionsSerializer(data=request.data)
        print(SessionsSerializer.errors)
        is_valid = session.is_valid()
        print(session.errors)
        if session.is_valid():
            session.save()
            return Response({'msg': 200})
        else:
            return Response({'msg': 404})
        
class AddMaterial(APIView):
    def post(self, request, format=None):
        material = LectureSerializer(data=request.data)
        
        is_valid = material.is_valid()
        print(material.errors)
        if material.is_valid():
            material.save()
            return Response({'msg': 200})
        else:
            return Response({'msg': 404})
        
        



    



  


