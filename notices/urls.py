from django.urls import path
from . import views

urlpatterns = [
    path('', views.notices, name='notices')
]