from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Course, Category
from tutor.models import Tutor
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from base.models import User
from tutor.models import Tutor
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from courses.models import Course,EnrolledCourse
from payment.serializers import EnrolledSerializer
from rest_framework.generics import ListCreateAPIView
from .serializers import CourseSerializer, CategorySerializer, PostCourseSerializer




class Cours(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    
class Categor(ListCreateAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    
class HomeListCourse(APIView):
    def get(self, request):
        queryset = Course.objects.filter(is_active=True)
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)


class CourseDeleteView(APIView):
    def delete(self, request, course_id):
        queryset = Course.objects.filter(id=course_id)
        queryset.delete()
        return Response({'msg': 'Course deleted successfully'})


class CourseUpdateView(APIView):
    def put(self, request, course_id):
        course = Course.objects.get(id=course_id)
        serializer = PostCourseSerializer(course, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Course updated successfully"})
        else:
            print(serializer.errors)
            return Response(serializer.errors)


class CreateCourse(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = PostCourseSerializer(data=request.data)
        print(serializer.is_valid())
        print(serializer.errors)
       
        
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Course created'}, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, course_id=None):
        if course_id is not None:
            queryset = Course.objects.get(id=course_id)
            serializer = PostCourseSerializer(queryset)
            return Response(serializer.data)
        return Response({'msg': 'Course not found'}, status=404)


class CategoryDeleteView(APIView):
    def delete(self, request, cat_id):
        queryset = Category.objects.get(id=cat_id)
        queryset.delete()
        return Response({'msg': 'Category deleted successfully'})


class CategoryUpdateView(APIView):
    def put(self, request, cat_id):
        category = Category.objects.get(id=cat_id)
        serializer = CategorySerializer(category, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Category updated successfully"})
        else:
            return Response(serializer.errors)


class CreateCategory(APIView):
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        print(serializer.is_valid())
        print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Category created'}, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, cat_id=None):
        if cat_id is not None:
            queryset = Category.objects.get(id=cat_id)
            serializer = CategorySerializer(queryset)
            return Response(serializer.data)
        return Response({'msg': 'Category not found'}, status=404)


class ApproveCourse(APIView):
    def get(self, request, tutor_id, pk):
        try:
            tutor = Tutor.objects.get(id=tutor_id)
            course = Course.objects.get(id=pk)
        except:
            raise NameError
        
        if not tutor:

            tutor = True
            tutor.save()
            
            if course.is_rejected:
                course.is_rejected = False
                course.save()
                
            course.is_approved = True
            course.save()

           
            return Response({'msg': 'User and course updated'})
        else:
            if course.is_rejected:
                course.is_rejected = False
                course.save()
            
            course.is_approved = True
            course.save()
            
            return Response({'msg': 'Course only updated'})
        

class RejectCourse(APIView):
    def delete(self, request, id):
        course = Course.objects.get(id=id)
        course.is_rejected = True
        course.save()
        return Response({'msg': 'Course rejected successfully'})
           

class BlockCourse(APIView):
    def get(self, request, pk):
        course = Course.objects.get(id=pk)
        course.is_approved = not course.is_approved
        course.save()
        return Response({'msg': 'Course block status updated'})
    

    

class MyCourses(APIView):
    def get(self,request,pk):
        id = User.objects.get(id=pk)
        mycourse = EnrolledCourse.objects.filter(user=id)
        serializer = EnrolledSerializer(mycourse, many=True)
        return Response(serializer.data)
    




