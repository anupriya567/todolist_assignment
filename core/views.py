from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . serializers import TaskListSerializer
from . models import Task
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated


class TaskVS(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['completed']

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(addedBy = user)
        return queryset
      
    
    def create(self, request, *args, **kwargs):
        task = request.data
        name = task.get('addedBy')

        try:      
           addedBy = User.objects.get(username = name)
        except Task.DoesNotExist or ValidationError:
            return Response({'addedBy': ["addedBy is invalid"]})
            
        serializer = TaskListSerializer(data = task)
        if serializer.is_valid():
            task = Task.objects.create(**serializer.validated_data, addedBy = addedBy)
            task.save()
            return Response(TaskListSerializer(task).data)
        return Response(serializer.errors)    
               


class ToogleCompletion(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        task = Task.objects.get(id = pk)
        task.completed^=True
        task.save()
        serializer = TaskListSerializer(task)
        return Response(serializer.data)
        



