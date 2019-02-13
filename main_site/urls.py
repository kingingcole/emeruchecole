from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name='index'),
    path('blermo/', views.blermo, name='blermo-work'),
    path('movieapp/', views.movie_app, name='movie-app-work'),

]