from django.shortcuts import render
from django.views import View


# class for about page
class About(View):
    def get(self, request):
        return render(request, 'about-us.html')
    
    
# class for contact page
class Contact(View):
    def get(self, request):
        return render(request, 'contact-us.html')
    
    
# class for 404 page
class Error404(View):
    def get(self, request):
        return render(request, '404.html')
    
    
# class for frequently asked questions page
class FAQ(View):
    def get(self, request):
        return render(request, 'faq.html')
    
    
# class for privacy policy page
class Privacy(View):
    def get(self, request):
        return render(request, 'privacy-policy.html')

# class for privacy policy page
class Discover(View):
    def get(self, request):
        return render(request, 'product-details-default.html')
    
# class for pabout-us page
class About(View):
    def get(self, request):
        return render(request, 'about-us.html')
    
    
