from rest_framework import serializers
from servicos_adicionais.models import Servicos_adicionais
from .models import Quarto

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicos_adicionais
        fields = ['id', 'tipo', 'descricao', 'valor']

class QuartoSerializer(serializers.ModelSerializer):
    servicos_adicionais = ServicoSerializer(many=True, read_only=True)

    class Meta:
        model = Quarto
        fields = [
            'numero', 'tipo', 'capacidade', 'preco_diaria',
            'descricao_detalhada', 'imagens', 'avaliacao',
            'servicos_adicionais'
        ]
