from django.shortcuts import render
from django.views import View

# class for account pages

class Login(View):
    def get(self , request):
        return render(request, 'login.html')