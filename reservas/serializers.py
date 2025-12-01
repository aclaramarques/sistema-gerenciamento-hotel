from rest_framework import serializers
from .models import Reserva
from clientes.models import Hospede
from quartos.models import Quarto

# Mantenha o ReservaSerializer (que é bom para leitura)
class ReservaSerializer(serializers.ModelSerializer):
    hospede_nome = serializers.CharField(source='hospede.nome', read_only=True)
    quarto_tipo = serializers.CharField(source='quarto.tipo', read_only=True)

    class Meta:
        model = Reserva
        fields = '__all__'

# CORRIJA ESTE AQUI:
class ReservaCreateSerializer(serializers.ModelSerializer):
    hospede = serializers.CharField()
    quarto = serializers.IntegerField()

    class Meta:
        model = Reserva
        fields = ['hospede', 'quarto', 'dtEntrada', 'dtSaida', 'quantPessoas']

    def to_representation(self, instance):
        return ReservaSerializer(instance).data

    def validate(self, data):
        # Validação do Hóspede
        cpf_hospede = data.get('hospede')
        if not Hospede.objects.filter(cpf=cpf_hospede).exists():
            raise serializers.ValidationError({"hospede": "Hóspede com este CPF não encontrado."})

        # Validação do Quarto
        id_quarto = data.get('quarto')
        # Ajuste se sua PK for 'numero' ou 'id'
        if not Quarto.objects.filter(pk=id_quarto).exists():
            raise serializers.ValidationError({"quarto": "Quarto com este ID não encontrado."})
            
        return data

    def create(self, validated_data):
        hospede_cpf = validated_data.pop('hospede')
        quarto_id = validated_data.pop('quarto')

        hospede_obj = Hospede.objects.get(cpf=hospede_cpf)
        quarto_obj = Quarto.objects.get(pk=quarto_id)

        reserva = Reserva.objects.create(
            hospede=hospede_obj,
            quarto=quarto_obj,
            **validated_data
        )
        return reserva