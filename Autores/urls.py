from django.urls import path

from . import views

urlpatterns = [
   path('', views.cadastrarAutor),
   path('listacadastro', views.listarAutor)
]