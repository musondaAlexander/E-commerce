from django.shortcuts import render

# Create your views here.

def home(reuest):
    return render(reuest, 'index.html')


def organic(request):
    return render(request, 'index-2.html')