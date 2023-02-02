from django.shortcuts import render
from  django.views import View


class ViewCert(View):
    def get(self, request):
        return render(request, 'cart_shop/cart.html')



class Wishlist(View):
    def get(self, request):
        return render(request, 'cart_shop/wishlist.html')
# Create your views here.
