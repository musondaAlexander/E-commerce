from django.urls import URLPattern, path
from .import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('index',views.home_two, name = 'index'),
     path('clothes',views.clothes, name = 'clothes'),
]
