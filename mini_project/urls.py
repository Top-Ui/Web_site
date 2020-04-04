"""mini_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from app_1 import views as app1_views
from app_2 import views as app2_views

urlpatterns = [
    path('', app1_views.home),
    path('send', app1_views.send_me),
    path('App', app2_views.startup_function),
    path('upload', app2_views.upload_function),
    path('text_editor', app2_views.texteditor_function),
    path('admin/', admin.site.urls),
]
