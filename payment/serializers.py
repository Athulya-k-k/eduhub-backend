from rest_framework import serializers

from .models import Order
from courses.models import EnrolledCourse

from base.serializers import UserSerializer
from courses.serializers import CourseSerializer
from learning.models import Progress


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
        depth = 2
        
        

        

        

class GetOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'
        

class EnrolledSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    course = CourseSerializer()
    class Meta:
        model = EnrolledCourse
        fields = '__all__'
        
class EnrolledCourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EnrolledCourse
        fields = '__all__'
        

class LearningSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Progress
        fields = '__all__'