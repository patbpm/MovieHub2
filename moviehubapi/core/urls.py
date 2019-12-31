from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('mostrated', views.mostrated, name='mostrated'),
    path('mostpopular', views.mostpopular, name='mostpopular'),
    path('searchmovie', views.searchmovie, name='searchmovie'),
    path('movie/(?P<pk>\d+)', views.movie_detail, name='movie_detail'),
    path('tvserie/(?P<pk>\d+)', views.tvserie_detail, name='tvserie_detail'),
    path('tvserie/(?P<pk>\d+)/season/(?P<season_number>\d+)', views.season_detail, name='season_detail'),
    path('tvserie/(?P<pk>\d+)/season/(?P<season_number>\d+)/episode/(?P<episode_number>\d+)', views.episode_detail, name='episode_detail'),
    path('person/(?P<pk>\d+)', views.person_detail, name='person_detail'),
]