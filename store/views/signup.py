from django.shortcuts import render
from django.views import View

# class for sign up pages
class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
