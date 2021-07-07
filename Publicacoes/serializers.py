from rest_framework import serializers
from .models import Publicacao


class PublicacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publicacao
        fields = ['url', 'author', 'title', 'description']
