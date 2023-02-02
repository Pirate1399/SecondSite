from django.urls import path
from .views import BlogSingle_View, Blog_View

app_name = 'blog'

urlpatterns = [
    path('', Blog_View.as_view(), name = 'blog'),
    path('blog-single', BlogSingle_View.as_view(), name = 'single-blog'),
]