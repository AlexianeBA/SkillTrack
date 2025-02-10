from rest_framework import routers
from apps.users.views import UserViewSet
from apps.employees.views import EmployeesViewSet, SkillViewSet, EmployeeSearchView

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'users', UserViewSet)
api.register(r'employees', EmployeesViewSet)
api.register(r'skills', SkillViewSet)

