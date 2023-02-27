from django.shortcuts import render
from django.views import View

# class for account pages

class Account(View):
    def get(self, request):
        return render(request, 'my-account.html')