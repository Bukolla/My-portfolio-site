
from django.urls import path
from . import views
urlpatterns = [
      path('', views.home, name='index'),
      path('blog.html/', views.Blog, name='blog'),
      path('blogpage.html/', views.Blog2, name='blogpage'),
      path('base.html/', views.contact, name='contact'),
]
