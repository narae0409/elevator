from rest_framework import serializers 
from .models import *

class MovieSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Elevator # 모델 설정 
        fields = ('id', 'number','date','acceleration','altitude', 'pir') # 필드 설정

class AddressSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Address # 모델 설정 
        fields = ('number','address') # 필드 설정


"""
class MovieSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta: 
        model = Data
        fields = ('id','time','sensor','measure')
"""