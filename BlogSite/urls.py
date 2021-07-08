from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Autores import views


router = DefaultRouter()
router.register(r'groups', views.GroupViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('Autores/', include('Autores.urls')),
    path('Publicacoes/', include('Publicacoes.urls'))
]
