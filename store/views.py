from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'store/index.html')

# for testing if the html file are loading 

def home_two(request):
    return render(request,'store/index-2.html')
def clothes(request):
    return render(request,'store/index-3.html')