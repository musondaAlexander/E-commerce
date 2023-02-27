from django.urls import path
from . import views

from .views.home import home
from .views.home import Home 

urlpatterns = [
    path('', Home.as_view(), name='home'),
    #  path('organic', views.organic , name='organic'),
    #  path('tech', views.tech, name='tech'),
    #  path('beauty', views.beauty, name='beauty'),
     
]
