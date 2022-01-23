from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path("blog-categorie/<str:pk>/", views.blogCategory, name='blog-categorie'),
    path('blog/<str:pk>/', views.blog, name='blog'),

]