from django.shortcuts import render
from django.views import View

# classes for wishlist

class Wishlist(View):
    def get(self, request):
        return render(request, 'wishlist.html')