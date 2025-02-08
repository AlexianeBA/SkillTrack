from rest_framework import serializers
from .models import Skill, Employees

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class EmployeesSerializer(serializers.ModelSerializer):
    skills = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(),
        many=True,
        write_only=True
    )
    skill_objects = SkillSerializer(many=True, source='skills', read_only=True)
    class Meta:
        model = Employees
        fields = ['id', 'first_name', 'last_name', 'email', 'position', 'skills', 'skill_objects', 'salary', 'hire_date']
    
    def create(self, validated_data):
        skills_data = validated_data.pop('skills', [])
        employee = Employees.objects.create(**validated_data)
        for skill_name in skills_data:
            skill, created = Skill.objects.get_or_create(name=skill_name)
            employee.skills.add(skill)
        return employee

    def update(self, instance, validated_data):
        skills_data = validated_data.pop('skills', [])
        instance = super().update(instance, validated_data)
        instance.skills.clear()
        for skill_name in skills_data:
            skill, created = Skill.objects.get_or_create(name=skill_name)
            instance.skills.add(skill)
        return instance