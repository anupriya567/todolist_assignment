from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Task
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'is_superuser']


class TaskListSerializer(ModelSerializer):
    addedBy = serializers.CharField(source = 'addedBy.username', read_only = True)
    class Meta:
        model = Task
        fields = '__all__'

