from django.db import models

class Hospede(models.Model):
    # CPF continua sendo a chave primária
    cpf = models.CharField(primary_key=True, max_length=14) 
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    
    # NOVOS CAMPOS PARA INTEGRAÇÃO
    email = models.EmailField(max_length=100, blank=True, null=True)
    uid_firebase = models.CharField(max_length=128, blank=True, null=True, unique=True)
    
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"