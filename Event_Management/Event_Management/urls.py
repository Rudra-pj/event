"""
URL configuration for Event_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from home import views
from django.conf import settings
from django.conf.urls import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('landing/', views.landing),
    path('createvent/', views.createvent),
    path('yourevents/', views.yourevents),
    path('deletevent/<int:eid>/', views.deletevent),
    path('viewdetails/<int:eid>/', views.viewdetails),
    path('editevent/<int:eid>/', views.editevent),
    path('book/<int:eid>/', views.book),
    path('yourtickets/', views.yourtickets),
    path('dashboard/<int:eid>/', views.dashboard),
    path('adminlogin/', views.adminlogin),
    path('adminlanding/', views.adminlanding)
    
]
