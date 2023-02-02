
from django.urls import path
from .views import IndexShopView, AboutView, Contacts

app_name = 'home'
urlpatterns = [
    path('', IndexShopView.as_view(), name = 'index'),
    path('about/', AboutView.as_view(), name = 'about'),
    path('contact/', Contacts.as_view(), name = 'contact'),
]