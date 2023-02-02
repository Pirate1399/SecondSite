from django.urls import path
from .views import Shop, SingleProducts

app_name = 'shop'
urlpatterns = [
    path('', Shop.as_view(), name = 'shop'),
    path('single_products/', SingleProducts.as_view(), name = 'product-single'),
    ]