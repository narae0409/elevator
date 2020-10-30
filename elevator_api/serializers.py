from rest_framework import serializers 
from .models import *

class MovieSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Elevator # 모델 설정 
        fields = ('number','date','acceleration','altitude') # 필드 설정


"""
class MovieSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta: 
        model = Data
        fields = ('id','time','sensor','measure')
"""