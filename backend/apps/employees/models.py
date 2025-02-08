from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employees(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skill, related_name="compétences")
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField(auto_now_add=True)
    cv = models.FileField(upload_to='cv/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"