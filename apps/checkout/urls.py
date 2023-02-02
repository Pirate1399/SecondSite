from django.urls import path
from .views import Checkout

app_name = 'checkout'

urlpatterns = [
    path('', Checkout.as_view(), name = 'checkout'),
]