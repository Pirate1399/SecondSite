from django.shortcuts import render
from django.views import View


class Blog_View(View):
    def get(self, request):
        return render(request, 'blog/blog.html')



class BlogSingle_View(View):
    def get(self, request):
        return render(request, 'blog/blog-single.html')

