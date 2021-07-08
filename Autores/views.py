from django.shortcuts import render, redirect
from django.shortcuts import render, get_list_or_404
from django.http import request
from .models import Cadastro
from .forms import AutorForm
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def cadastrarAutor(request):
    if request.method == "POST":
        form1 = AutorForm(request.POST)
        if form1.is_valid():
            form1.save()
            try:
                return redirect(listarAutor)
            except:
                pass
    else:
        form1 = AutorForm()
    return render(request, 'form.html', {'form': form1})


def listarAutor(request):
    post = get_list_or_404(Cadastro)
    return render(request, 'list_form.html', {'post': post})
