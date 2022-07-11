from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors/', views.show_all_directors),
    path('directors/<int:id>', views.show_one_director, name='director-detail'),
    path('actors/', views.show_all_actors),
    path('actors/<int:id>', views.show_one_actor, name='actor-detail'),
]