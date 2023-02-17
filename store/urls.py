from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('organic', views.organic , name='organic'),
     path('tech', views.tech, name='tech'),
     path('beauty', views.beauty, name='beauty'),
     
]
