from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('livros/',views.get_livros, name='get_livros'),
    path('autores/',views.get_autores, name='get_autores'),
    path('livros/<int:id>', views.get_livro_by_id ),
    path('autores/<int:id>', views.get_autor_by_id ),
    path('data_livro', views.livro_manager),
     path('data_autor', views.autor_manager),
     path('delete_autor/<int:autor_id>', views.delete_autor),
     path('delete_livro/<int:livro_id>', views.delete_livro),
]