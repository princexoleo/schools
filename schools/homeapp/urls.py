from django.contrib import admin
from django.urls import path,include
from homeapp import views

urlpatterns = [
    path('', views.home,name='home'),
    #path('home/', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('photo_gallery/', views.photo_gallery,name='gallery'),
    path('video_gallery/', views.video_gallery,name='video'),
    path('social_activities/', views.social_activities,name='social'),
    path('type/', views.type,name='type'),
    path('criteria/', views.criteria,name='criteria'),
    path('history/', views.history,name='history'),
    path('membership/', views.membership,name='membership'),
    path('eventpage/', views.eventpage,name='eventpage'),
    path('scholarship/', views.scholarship,name='scholarship'),
    path('committe/', views.committe,name='committe'),
]
