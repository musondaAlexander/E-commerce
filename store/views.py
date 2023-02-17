from django.shortcuts import render

# Create your views here.

# To handle home equipment  
def home(reuest):
    return render(reuest, 'index.html')

# to ahndle Organic 
def organic(request):
    return render(request, 'index-2.html')
#  to handle tech
def tech(request):
    return render(request, 'index-3.html')
# TO handle beauty 
def beauty(request):
    return render(request, 'index-4.html')