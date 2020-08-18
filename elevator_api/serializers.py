from rest_framework import serializers 
from .models import Data

class MovieSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Data # 모델 설정 
        fields = ('id','sensor','measure') # 필드 설정