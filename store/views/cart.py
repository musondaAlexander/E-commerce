from django.shortcuts import render
from django.views import View

# class for account pages

class Cart(View):
    def get(self , request):
        return render(request, 'cart.html')