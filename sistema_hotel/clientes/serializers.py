
from rest_framework import serializers
from .models import Hospede

class HospedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospede
        fields = '__all__'


class HospedeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospede
        fields = [
            'cpf',
            'nome',
            'telefone',
            'ativo',
        ]
