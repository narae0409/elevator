from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import xmltodict
import json


class DataList(APIView):

    def get_object(self, pk):
        try:
            return Elevator.objects.filter(number=pk)
        except Elevator.DoesNotExist:
            raise Http404
        
    def get(self, request, format=None):
        dt = Elevator.objects.all()
        serializer = MovieSerializer(dt, many=True)
        #DB data serializer를 통한 json화, xml file은 python module xmltodict 
        return Response(serializer.data)

    def post(self, request, format=None):
        val = request.data.values()
        if val is not None:
            for i in val:
                snippet = self.get_object(i)
                serializer = MovieSerializer(snippet, many=True)

        return Response(serializer.data)

class DataAddress(APIView):

    def get_object(self, pk):
        try:
            return Address.objects.filter(address__icontains=pk)
        except Address.DoesNotExist:
            raise Http404
        
    def get(self, request, format=None):
        dt = Address.objects.all()
        serializer = AddressSerializer(dt, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        val = request.data.values()
        if val is not None:
            for i in val:
                snippet = self.get_object(i)
                serializer = AddressSerializer(snippet, many=True)

        return Response(serializer.data)

class Detail(APIView):
        
    def get(self, request, format=None):
        dt = Elevator.objects.all()
        serializer = MovieSerializer(dt, many=True)
        #DB data serializer를 통한 json화, xml file은 python module xmltodict 
        return Response(serializer.data)

    def post(self, request, format=None):
        val = request.data.values()
        if val is not None:
            try:
                for number in val:
                    url = ("http://openapi.elevator.go.kr/openapi/service/ElevatorInformationService/getElevatorView?ServiceKey=u3HLRFEoHaS%2FlgLfJlPvGLg5kGfhz87aPtzuagSqXRXSBf%2FCQBoinqONsiA6DvKH6CEWzctUDuHw7ksE3Dyq5g%3D%3D&elevator_no=" + str(number))
                    res = requests.get(url)
                    #print(res.status_code)
                    #print(res.text)

                    cc = xmltodict.parse(res.text)
                    dd = json.loads(json.dumps(cc))
                    animals = dd['response']['body']
                    data = animals.values()
                    for i in data:
                        dict1 = {}
                        dict1=i
                    #print(dict1)
                    address = (dict1['address1'] + ' ' + dict1['buldNm'] + ' ' + dict1['elvtrAsignNo'])
                    Address.objects.update_or_create(number=number, address=address)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST) 

        return Response(dict1)


class DataInsert(APIView):

    def get(self, request, format=None):
        dt = Elevator.objects.all()
        serializer = MovieSerializer(dt, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        val = request.data.values()
        arr = list(val)
        dict1 = {"msg":"fail"}
        if arr[0] is not None:
            try:
                # ('number'=0,'humidity'=1, 'tempareture'=2, 'ir'=3,'acceleration_x'=4,'acceleration_y'=5,'acceleration_z'=6,'roll'=7, 'pitch'=8, 'yaw'=9, 'base_altitude'=10, 'current_altitude'=11, 'height'=12, 'permission_number'=13)
                dict1 = {"number":arr[0], "humidity":arr[1],"tempareture":arr[2], "ir":arr[3], "acceleration_x":arr[4], "acceleration_y":arr[5], "acceleration_z":arr[6], "roll":arr[7], "pitch":arr[8], "yaw":arr[9], "base_altitude":arr[10], "current_altitude":arr[11], "height":arr[12], "permission_number":arr[13]}
                Elevator.objects.create(number=arr[0], ir=arr[3], acceleration_x=arr[4], acceleration_y=arr[5], acceleration_z=arr[6], roll=arr[7], pitch=arr[8], yaw=arr[9], base_altitude=arr[10], current_altitude=arr[11], height=arr[12], permission_number=arr[13])  # dict1 = {"msg":"success"}
                return Response(dict1)
            except IndexError:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            #serializer = UserSerializer(snippet, many=True)

        return Response(dict1)

class NewUser(APIView):

    def get_object(self, pk):
        try:
            return User.objects.filter(my_id=pk)
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, format=None):
        dt = User.objects.all()
        serializer = UserSerializer(dt, many=True)
        #DB data serializer를 통한 json화, xml file은 python module xmltodict 
        return Response(serializer.data)

    def post(self, request, format=None):
        val = request.data.values()
        arr = list(val)
        dict1 = {"msg":"fail"}
        if arr[0] is not None:
            snippet = self.get_object(arr[0])
            for i in snippet.iterator():
                try:
                    if i.password == arr[1]:
                        dict1 = {"msg":"success"}
                except IndexError:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            #serializer = UserSerializer(snippet, many=True)

        return Response(dict1)

"""

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        print(serializer)
        print(serializer.pir)
        print(type(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #새로 입력할 데이터의 pk가 DB에 존재한다면 새로 저장이 아닌 데이터 변경으로 구현할 것.

class NewUser(APIView):

    def get_object(self, pk):
        try:
            return User.objects.filter(my_id=pk)
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, format=None):
        dt = User.objects.all()
        serializer = UserSerializer(dt, many=True)
        #DB data serializer를 통한 json화, xml file은 python module xmltodict 
        return Response(serializer.data)

    def post(self, request, format=None):
        val = request.data.values()
        if val is not None:
            for i in val:
                snippet = self.get_object(i)
                serializer = UserSerializer(snippet, many=True)

        return Response(serializer.data)


    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""