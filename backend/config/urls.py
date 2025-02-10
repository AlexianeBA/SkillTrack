from django.shortcuts import redirect
from django.urls import path
from django.contrib import admin
from django.contrib.auth import logout

from django.conf.urls import include

from config.api import api
from django.conf import settings
from django.conf.urls.static import static
from apps.employees.views import EmployeeSearchView


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', logout, {'next_page': '/'}, name='logout'),
    path("", lambda request: redirect('/api/login', permanent=True)),
    path('api/', include(api.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/users/', include('apps.users.urls')),
   path('api/search/', EmployeeSearchView.as_view(), name='employee_search'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
