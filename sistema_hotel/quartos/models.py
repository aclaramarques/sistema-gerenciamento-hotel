from django.db import models
from servicos_adicionais.models import Servicos_adicionais

class Quarto(models.Model):
    numero = models.IntegerField(unique=True, primary_key=True)
    tipo = models.CharField(max_length=50)
    capacidade = models.IntegerField()
    disponibilidade = models.BooleanField(default=True)
    preco_diaria = models.DecimalField(max_digits=8, decimal_places=2)
    
    descricao_detalhada = models.TextField()  
    imagens = models.ImageField(upload_to='quartos/%Y/%m/%d/', null=True, blank=True)  
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1, default=0)  

    servicos_adicionais = models.ManyToManyField(
        Servicos_adicionais,
        blank=True,
        related_name='quartos'
    )

    def __str__(self):
        return f"Quarto nº {self.numero} - {self.tipo}"
