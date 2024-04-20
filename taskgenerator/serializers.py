from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"

class TaskGeneratorSerializer(serializers.ModelSerializer):

    Brief = serializers.CharField(read_only=True)  

    class Meta:
        model = Taskgenerator
        fields = ['Role', 'Industry', 'Difficulty', 'Duration', 'Brief']

    # def create(self, validated_data):
    #     role = validated_data.get('Role')
    #     industry = validated_data.get('Industry')
    #     difficulty = validated_data.get('Difficulty')

    #     try:
    #         admin = Admin.objects.get(Role=role, Industry=industry, Difficulty=difficulty)
    #         validated_data['Brief'] = admin.Brief
    #     except Admin.DoesNotExist:
    #         validated_data['Brief'] = "Add the required text brief"  # Default message if no matching Admin object found

    #     return super().create(validated_data)