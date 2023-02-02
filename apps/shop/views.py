from django.shortcuts import render
from django.views import View

class Shop(View):
    def get(self, request):
        return render(request, 'shop/shop.html')

# Create your views here.
class SingleProducts(View):
    def get(self, request):
        return render(request, 'shop/product-single.html')