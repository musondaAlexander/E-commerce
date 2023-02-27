from django.shortcuts import render
from django.views import View

# classes for checkout 

class Checkout(View):
    def get(self, request):
        return render(request, 'checkout.html')
