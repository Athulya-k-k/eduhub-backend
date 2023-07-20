from rest_framework import serializers
from courses.models import Course,Category





        

class CategorySerializer(serializers.ModelSerializer):
    Category
    class Meta:
        model = Category
        fields = ['id','name','description','image']


class CourseSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model = Course
        fields = '__all__'


class PostCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [ 'title',  'description', 'category', 'image', 'video', 'price']



        



        

        