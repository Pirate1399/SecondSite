from django.shortcuts import render
from django.views import View

class IndexShopView(View):
    def get(self, request):
        return render(request, 'home/index.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'home/about.html')

class Contacts(View):
    def get(self, request):
        return render(request, 'home/contact.html')