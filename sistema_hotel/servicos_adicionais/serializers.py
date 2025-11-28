from rest_framework import serializers
from .models import Servicos_adicionais


class ServicosAdicionaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servicos_adicionais
        fields = '__all__'


class ServicosAdicionaisCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servicos_adicionais
        fields = [
            'tipo',
            'descricao',
            'valor'
        ]
