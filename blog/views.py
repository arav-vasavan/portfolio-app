from django.shortcuts import render,get_object_or_404          #get_object_or_404 ka use hm isliye krte hai taaki unknown url enter krne se error show ho page me.
from .models import Blog
# Create your views here.

def home_blog(request):
    blogs = Blog.objects.order_by('-date') #[:4]
    return render(request, 'blog_html/home_blog.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)   #pk matlb private key  jo ki blog id rhegi
    return render(request, 'blog_html/detail.html', {'blog':blog})