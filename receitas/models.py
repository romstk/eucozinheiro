from django.db import models
# Criação das classes de modelo que herdarão a classe models 

class Receita(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    ingredientes = models.TextField(null=False, blank=False)
    preparo = models.TextField(null=False, blank=False)
    imagem =models.CharField(max_length=150, null=False, blank=False)
    autor=models.CharField(max_length=150, null=False, blank=False)
    data = models.DateTimeField(auto_now_add=True) #fará seja armazenada data e hora da inserção do registro. 
    
