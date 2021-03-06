from rest_framework import serializers 
from .models import *

class MovieSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Elevator # 모델 설정 
        fields = ('id', 'number','date', 'ir','acceleration_x','acceleration_y','acceleration_z','roll', 'pitch', 'yaw', 'base_altitude', 'current_altitude', 'height', 'permission_number') # 필드 설정

class AddressSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Address # 모델 설정 
        fields = ('number','address') # 필드 설정

class UserSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = User # 모델 설정 
        fields = ('my_id','password', 'permission_number', 'agency') # 필드 설정

# fields에 포함되지 않는 columns는 DB에 저장되지도 않는다.

"""
class MovieSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta: 
        model = Data
        fields = ('id','time','sensor','measure')
"""