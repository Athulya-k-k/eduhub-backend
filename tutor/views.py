from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from base.models import User
from rest_framework import generics 
from rest_framework import permissions
from .models import Tutor
from rest_framework.decorators import api_view
from .serializers import TutorSerializer
from django.views.decorators.csrf import csrf_exempt

from .serializers import  TutorSerializer
from . import models

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

# Create your views here.



class TeacherList(generics.ListCreateAPIView):
   queryset = Tutor.objects.all()
   serializer_class = TutorSerializer
   

    

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Tutor.objects.all()
   serializer_class = TutorSerializer


class TutorLogin(APIView):
    def post(self, request):
        email = request.POST.get('email')
        if email is None:
            return Response({'bool': False, 'message': 'Email is missing'})

        password = request.POST.get('password')
        if password is None:
            return Response({'bool': False, 'message': 'Password is missing'})

        teacherData = Tutor.objects.filter(email=email, password=password).exists()
        if teacherData:
            return Response({'bool': True})
        
        return Response({'bool': False, 'message': 'Invalid email or password'})


class BlockTutorView(APIView):
    def put(self, request, tutor_id):
        try:
            print(tutor_id)
            tutor = Tutor.objects.get(id=tutor_id)
            tutor.is_active = False
            tutor.save()
            return Response({'message': 'Tutor blocked'})
        except Tutor.DoesNotExist:
            return Response({'message': 'Tutor not found'}, status=status.HTTP_404_NOT_FOUND)

class UnblockTutorView(APIView):
    def put(self, request, tutor_id):
        try:
            tutor = Tutor.objects.get(id=tutor_id)
            tutor.is_active = True
            tutor.save()
            return Response({'message': 'Tutor unblocked'})
        except Tutor.DoesNotExist:
            return Response({'message': 'Tutor not found'}, status=status.HTTP_404_NOT_FOUND)
