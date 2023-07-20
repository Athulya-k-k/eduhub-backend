from rest_framework import serializers\
    
from learning.models import Progress,Review
from csession.serializers import LectureSerializer,SingleLectureSerializer
from base.serializers import UserSerializer


class ProgressSerializer(serializers.ModelSerializer):
    lecture = SingleLectureSerializer()
    
    class Meta:
        model = Progress
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
        

class GetReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Review
        fields = '__all__'