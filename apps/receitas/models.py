from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
# Criação das classes de modelo que herdarão a classe models 

class Receita(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    ingredientes = models.TextField(null=False, blank=False)
    preparo = models.TextField(null=False, blank=False)
    imagem =models.ImageField(upload_to="fotos", blank=True)

    #campo autor associado a tabela de usuários para armazenarmos o usuário logado como o autor da receita.
    #on_delete - caso o usuário seja deletado vamos atribuir null a este campo
    #null=True, significa que o campo aceitará o valor null
    #related_name="user" , este campo serve para para facilitar a localização de tabelas e funcionalidades
    autor=models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )
    data = models.DateTimeField(default=datetime.now, blank=False) #fará com que seja armazenada data e hora da inserção do registro. 
    publicada = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Receita [nome={self.nome}]"