from django import forms
from .models import Quarto
from servicos_adicionais.models import Servicos_adicionais

class QuartoForm(forms.ModelForm):
    servicos_adicionais = forms.ModelMultipleChoiceField(
        queryset=Servicos_adicionais.objects.all(),
        widget=forms.CheckboxSelectMultiple, 
        required=False
    )

    class Meta:
        model = Quarto
        fields = [
            'numero', 'tipo', 'capacidade', 'preco_diaria',
            'descricao_detalhada', 'imagens', 'avaliacao', 'servicos_adicionais'
        ]
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'preco_diaria': forms.NumberInput(attrs={'class': 'form-control'}),
            'descricao_detalhada': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'avaliacao': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.1, 'min': 0, 'max': 5}),
        }
