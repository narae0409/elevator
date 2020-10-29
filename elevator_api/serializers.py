from rest_framework import serializers 
from .models import Data

class MovieSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Data # 모델 설정 
        fields = ('id','time','sensor','measure') # 필드 설정


"""
class MovieSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta: 
        model = Data
        fields = ('id','time','sensor','measure')
"""