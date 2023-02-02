from django.urls import path
from .views import ViewCert, Wishlist

app_name = 'cart_shop'
urlpatterns = [
    path('', ViewCert.as_view(), name = 'cart'),
    path('wishlist/', Wishlist.as_view(), name = 'wishlist'),
    ]