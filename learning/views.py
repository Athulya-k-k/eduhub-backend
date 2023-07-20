from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from courses.models import EnrolledCourse
from csession.models import Lecture
from .models import Progress,Review
from .serializers import ProgressSerializer,ReviewSerializer,GetReviewSerializer
from courses.models import Course
from base.models import User

class ProgressView(APIView):
    def get(self, request, pk,id):
        user = User.objects.get(id=id)
        course = EnrolledCourse.objects.get(course=pk,user=user)
        lectures = Progress.objects.filter(current_course=course,user=user)
        
        serializer = ProgressSerializer(lectures, many=True)
        return Response(serializer.data)
    
class GetProgress(APIView):
    def get(self, request, pk,id):
        user = User.objects.get(id=id)
        course = EnrolledCourse.objects.get(course=pk,user=user)
        
        progress = course.courseprogress
        return Response(progress)
    
    
    
class UpdateProgress(APIView):
    def get(self, request, pk,id):
        user = User.objects.get(id=id)
        course = EnrolledCourse.objects.get(course=pk,user=user)
        lectures = Progress.objects.filter(current_course=course,user=user)
        total = lectures.count()
        for index,i in enumerate(lectures):
            if i.is_active == True:
                print(i)
                i.is_completed = True
                i.save()
                
                if index+1==total:
                    break
                else:
                    next_object = lectures[index + 1]
                    next_object.is_active= True
                    next_object.save()
                    
                    i.is_active = False
                    i.save()
                    
                    print("updated....")
                    break
            
        total = lectures.count()
        print(total)
        current_percentage = course.courseprogress
        if current_percentage=="100.0":
            print("completed")
        else:
            percentage = float((1/float(total))*100)
            course.courseprogress = float(current_percentage)+percentage
            course.save()
        
        return Response({'msg':200})
    
class GetReview(APIView):
    def get(self, request, pk):
        course = Course.objects.get(id=pk)
        reviews = Review.objects.filter(course=course)

        
        serializer = GetReviewSerializer(reviews,many=True)
        # print(serializer.errors)
        return Response(serializer.data)
    
class AddReview(APIView):
    def post(self, request, format=None):
        print(request.data)
        print(request.data.get('course'))
        
        review = ReviewSerializer(data=request.data)
        is_valid = review.is_valid()
        print(review.errors)

        if review.is_valid():
            review.save()
            return Response({'msg': 200})
        else :
            return Response({'msg': 404})