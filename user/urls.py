from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('account/', views.userAccount, name="account"),

    path('executive-committee/', views.executiveCommittees, name='executive-committees'),
    path('executive-committee/<str:pk>/', views.executiveCommittee, name='executive-committee'),
    path('moderators/', views.moderators, name='moderators'),
    path('moderator/<str:pk>/', views.moderator, name='moderator'),

    path('edit-account/', views.editAccount, name="edit-account"),

    path('create-skill/', views.createSkill, name="create-skill"),
    path('update-skill/<str:pk>/', views.updateSkill, name="update-skill"),
    path('delete-skill/<str:pk>/', views.deleteSkill, name="delete-skill"),

    path('create-education/', views.createEducation, name="create-education"),
    path('update-education/<str:pk>/', views.updateEducation, name="update-education"),
    path('delete-education/<str:pk>/', views.deleteEducation, name="delete-education"),

    path('create-experience/', views.createExperience, name="create-experience"),
    path('update-experience/<str:pk>/', views.updateExperience, name="update-experience"),
    path('delete-experience/<str:pk>/', views.deleteExperience, name="delete-experience"),

    path('search-me/', views.searchMe, name='search-me'),
    path('blood-search/', views.bloodSearch, name="blood-search"),

    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.viewMessage, name="message"),
    path('create-message/<str:pk>/', views.createMessage, name="create-message"),
]