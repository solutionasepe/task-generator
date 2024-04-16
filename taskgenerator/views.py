from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.http import HttpResponse
import json

# Create your views here.
class AdminAPIViews(generics.ListCreateAPIView): 
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class TaskGeneratorAPIViews(generics.CreateAPIView):
    queryset = Taskgenerator.objects.all()
    serializer_class = TaskGeneratorSerializer

    
    def perform_create(self, serializer):
        # Extract data from request
        Role = self.request.data.get('Role')
        Industry = self.request.data.get('Industry')
        Difficulty = self.request.data.get('Difficulty')

        
        # Retrieve Admin object based on extracted data
        admin = Admin.objects.get(Role=Role, Industry=Industry, Difficulty=Difficulty)
        Brief = admin.Brief

        # Save the serializer and retrieve the Brief
        serializer.save(Brief=Brief)
        return super().perform_create(serializer)
    

        

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try: 
            self.perform_create(serializer)
            serializer_data = serializer.data
            brief_data = serializer_data['Brief']
            
            response_data = {"Brief": brief_data}
            print(response_data)

            return Response(response_data)
        except Admin.DoesNotExist:
            return Response({'error':'brief not found'}, status=status.HTTP_404_NOT_FOUND)    
        
    

        
        