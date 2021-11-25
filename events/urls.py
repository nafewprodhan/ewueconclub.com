from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirectEvents),
    path('event/', views.redirectEvents),

    path('event-categories/', views.events, name="events"),
    path("event-categories/<str:pk>/", views.eventCategory, name='event-categories'),
    path('event/<str:pk>/', views.event, name='event'),
]