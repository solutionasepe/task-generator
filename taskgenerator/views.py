from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.http import HttpResponse
import json
import random

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
        Duration = self.request.data.get('Duration')
        
        # Retrieve Admin object based on extracted data
        admin = Admin.objects.filter(Role=Role, Industry=Industry, Difficulty=Difficulty, Duration=Duration)
        # Brief = admin.Brief

        #Getting the list of more than one admin instance
        admin_list = []
        if Admin.objects.count() > 1:
            for admin in Admin.objects.all():
                admin_list.append(admin)
            admin = random.choice(admin_list)
            Brief = admin.Brief
        # Save the serializer and retrieve the Brief
        else:
            admin = Admin.objects.first()
            Brief = admin.Brief
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
        
    

        
        