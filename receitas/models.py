from django.db import models

from datetime import datetime
# Criação das classes de modelo que herdarão a classe models 

class Receita(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    ingredientes = models.TextField(null=False, blank=False)
    preparo = models.TextField(null=False, blank=False)
    imagem =models.ImageField(upload_to="fotos", blank=True)
    autor=models.CharField(max_length=150, null=False, blank=False)
    data = models.DateTimeField(default=datetime.now, blank=False) #fará seja armazenada data e hora da inserção do registro. 
    publicada = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Receita [nome={self.nome}]"