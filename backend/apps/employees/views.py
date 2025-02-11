from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Skill, Employees
from .serializers import SkillSerializer, EmployeesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class EmployeeSkillSearchView(APIView):
    def get(self, request, *args, **kwargs):
        skills = request.GET.getlist('skills')
        #utilisation de Q objects pour construire une requête de recherche insenssible à la casse
        query = Q()
        for skill in skills:
            query |= Q(skills__name__icontains=skill)
        employees = Employees.objects.filter(query).distinct()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EmployeeSearchByNameView(APIView):
    def get(self, request, *args, **kwargs):
        name = request.GET.get('name', '')
        query = Q()
        for term in name.split():
            query |= Q(first_name__icontains=term) | Q(last_name__icontains=term)
        employees = Employees.objects.filter(query).distinct()
        serializer = EmployeesSerializer(employees.distinct(), many=True)
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
