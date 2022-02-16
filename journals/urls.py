from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.journals, name="journals"),
    path('journal/<str:pk>', views.journal, name='journal'),
]

