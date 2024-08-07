from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('/author_profile', views.author_profile, name='perfil'),
    path('/book_reading', views.book_reading, name='livros'), 
    path('/projects_created', views.projects_created, name='projetos'),
    path('/programs_used', views.programs_used, name='programas'),
    path('/maintenance', views.maintenance, name='manutenção'),
    path('', views.create_empresa, name='create_empresa'),
]