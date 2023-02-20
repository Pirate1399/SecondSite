from django.shortcuts import render
from django.views import View
from apps.cart_shop.models import Product, Wishlist

class IndexShopView(View):
    def get(self, request):
        data = Product.objects.all()
        wish = Wishlist.objects.filter(wishlist__user=request.user)
        wishname = [i.product.name for i in wish]
        context = {'data': data, 'wishlist_items': wishname}
        return render(request, 'home/index.html', context)

class AboutView(View):
    def get(self, request):
        return render(request, 'home/about.html')

class Contacts(View):
    def get(self, request):
        return render(request, 'home/contact.html')