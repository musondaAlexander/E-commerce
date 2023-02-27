from django.shortcuts import render
from django.views import View

#  The home class 
class Home(View):
    def get(self, request):
        return render(request, 'index.html')