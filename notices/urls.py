from django.urls import path
from . import views

urlpatterns = [
    path('', views.notices, name='notices'),
    path('notice/<str:pk>', views.notice, name="notice")
]