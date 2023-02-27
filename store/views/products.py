from django.shortcuts import render
from django.views import View

# class for affiliate product

class ProductDetailsAffliate(View):
    def get(self, request):
        return render(request, 'product-details-affiliate.html')
    
    
    # class for deafult product
class ProductDetailsDefault(View):
    def get(self, request):
        return render(request, 'product-details-default.html')
    
    
    # class for groupt product
class ProductDetailsGroup(View):
    def get(self, request):
        return render(request, 'product-details-group.html')
    
    
    # class for product variable 
class ProductDetailsVariable(View):
    def get(self, request):
        return render(request, 'product-details-variable.html')

# Class for compare product
class Compare(View):
    def get(self, request):
        return render(request, 'compare.html')

