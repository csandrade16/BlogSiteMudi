from django.urls import path
from . import views

urlpatterns = [
   path('cadastro', views.cadastrarAutor),
   path('listacadastro', views.listarAutor)
    ]