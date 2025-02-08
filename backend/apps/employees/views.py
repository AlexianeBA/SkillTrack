from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Skill, Employees
from .serializers import SkillSerializer, EmployeesSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
        
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)