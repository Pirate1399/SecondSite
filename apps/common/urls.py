from django.urls import path
from .views import CurrentDateView, Hello, IndexView

urlpatterns = [
    path("", IndexView.as_view()),
    path("datetime/", CurrentDateView.as_view()),
    path('hello/', Hello.as_view()),

]