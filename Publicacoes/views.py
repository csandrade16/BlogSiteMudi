from Publicacoes.models import Publicacao
from .serializers import PublicacaoSerializer
from django.http import request, Http404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Publicacao
from rest_framework import generics

class PublicationsViewSet(viewsets.ModelViewSet):
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer



class PublicacaoList(APIView):
    """
    List all Publications, or create a new Publication.
    """

    def get(request, format=None):
        posts = Publicacao.objects.all()
        serializer = PublicacaoSerializer(posts, many=True)
        return Response(serializer.data)

    def post(request, format=None):
        serializer = PublicacaoSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicacaoDetail(APIView):
        def get_object(self, pk):
                try:
                   return Publicacao.objects.get(pk=pk)
                except Publicacao.DoesNotExist:
                    raise Http404



class PostList(generics.ListAPIView):
    serializer_class = PublicacaoSerializer

    def get_queryset(self):

        author = self.request.author
        title = self.request.title
        description = self.request.description
        return Publicacao.objects.filter(author=author, title=title, description=description)


