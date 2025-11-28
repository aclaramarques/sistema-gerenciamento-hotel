from rest_framework import serializers
from .models import Reserva
from clientes.models import Hospede
from quartos.models import Quarto

class ReservaCreateSerializer(serializers.ModelSerializer):
    hospede = serializers.CharField()
    quarto = serializers.IntegerField()

    class Meta:
        model = Reserva
        fields = [
            'hospede',
            'quarto',
            'dtEntrada',
            'dtSaida',
            'quantPessoas',
        ]

    def create(self, validated_data):
        hospede_cpf = validated_data.pop('hospede')
        quarto_id = validated_data.pop('quarto')

        hospede = Hospede.objects.get(cpf=hospede_cpf)
        quarto = Quarto.objects.get(id=quarto_id)

        reserva = Reserva.objects.create(
            hospede=hospede,
            quarto=quarto,
            **validated_data
        )

        return reserva


class ReservaSerializer(serializers.ModelSerializer):
    hospede = serializers.StringRelatedField()
    quarto = serializers.StringRelatedField()

    class Meta:
        model = Reserva
        fields = '__all__'