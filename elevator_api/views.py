from .models import Data 
from .serializers import MovieSerializer 
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DataList(APIView):


    def get_object(self, pk):
        try:
            return Data.objects.filter(sensor=pk)
        except Data.DoesNotExist:
            raise Http404
        
    def get(self, request, format=None):
        dt = Data.objects.all()
        serializer = MovieSerializer(dt, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        val = request.data.values()
        if val is not None:
            for i in val:
                snippet = self.get_object(i)
                serializer = MovieSerializer(snippet, many=True)
        return Response(serializer.data)


class DataInsert(APIView):

    def get(self, request, format=None):
        dt = Data.objects.all()
        serializer = MovieSerializer(dt, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""