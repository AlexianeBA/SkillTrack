from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Skill, Employees
from .serializers import SkillSerializer, EmployeesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class EmployeeSearchView(APIView):
    def get(self, request, *args, **kwargs):
        skills = request.GET.getlist('skills')
        employees = Employees.objects.filter(skills__name__in=skills).distinct()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
        
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
