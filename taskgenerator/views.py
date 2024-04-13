from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class AdminAPIViews(generics.ListCreateAPIView): 
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class TaskGeneratorAPIViews(generics.CreateAPIView):
    queryset = Taskgenerator.objects.all()
    serializer_class = TaskGeneratorSerializer

    
    def perform_create(self, serializer):
        Role = self.request.data.get('Role')
        Industry = self.request.data.get('Industry')
        Difficulty = self.request.data.get('Difficulty')

        try:
            admin = Admin.objects.get(Role=Role, Industry=Industry, Difficulty=Difficulty)
            Brief = admin.Brief
            # Set the user field to the currently logged-in user
            serializer.save(Brief=Brief)
            serializer_brief = serializer.validated_data.get('Brief')
            return Response(data=serializer_brief)
        except Admin.DoesNotExist:
            return Response({'error': 'brief not found'}, status=status.HTTP_404_NOT_FOUND)