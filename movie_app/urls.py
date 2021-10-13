from django.urls import path
from . import views

app_name = 'movie_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:id>/', views.movie_detail, name='detail'),
    path('update/<int:id>/', views.update_movie, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('add/', views.add_movie, name='add'),
]
