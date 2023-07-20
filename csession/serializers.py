from rest_framework import serializers
from .models import Sessions,Lecture
from courses.models import Course
from courses.serializers import CategorySerializer
from base.serializers import UserSerializer

        
        
class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'
        
        
class CourseSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Course
        fields = '__all__'

        
class SessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessions
        fields = '__all__'
        

        

        
        

class SingleLectureSerializer(serializers.ModelSerializer):
    session = SessionsSerializer() 
    course = CourseSerializer()
    
    class Meta:
        model = Lecture
        fields = '__all__'
  
        