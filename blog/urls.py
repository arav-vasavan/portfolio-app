from django.urls import path, include
from . import views

app_name = 'blog_app' #application ka name define kr diye yaha

urlpatterns = [
    path('', views.home_blog, name="home_blog"),
    path('<int:blog_id>/', views.detail, name="detail"),    
    #int:blog_id  ka use url me jaane ke liye karenge particular blog ke id ke through aur detail function hmko milega views.py me

]