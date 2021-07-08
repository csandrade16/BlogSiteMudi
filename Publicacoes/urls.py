from .views import PublicacaoList, PublicacaoDetail
from django.urls import path

urlpatterns = [
    path('publications-list/', PublicacaoList.as_view()),
    path('publications-detail/', PublicacaoDetail.as_view())
]