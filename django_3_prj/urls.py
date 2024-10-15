"""
URL configuration for django_3_prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from crud_app import views

urlpatterns = [
    path('classbase/', include('classbase_crud_app.urls')),
    path('drf_api/', include('drf_crud_app.urls')),
    path('admin/', admin.site.urls),
    path('index/', views.launch_form, name="index"),
    path('index/create', views.create_data, name="create_url"),
    path('show/', views.show_details, name="show_url"),
    path('show/delete/<num>', views.delete_data, name="delete_url"),
    path('show/update/<num>', views.update_form, name="update_form_url"),
    path('show/update_2/<num>', views.update_data, name="update_data_2"),
]

a = 10
num = 14