from rest_framework import serializers
from .models import Cart
from courses.serializers import CourseSerializer



class AddCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        

class GetCartSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = Cart
        fields = '__all__'
        

