from django.db import models
from django.contrib.auth.models import AbstractUser
# Classe que abstai o user do auth_user
# Camppos que são padrão do auth_user que já existem por padrão já vem # como padrão para esta classe bastando inserir os campos adicionais. 
# id, password, last_login, is_superuser, username, last_name, email
# is_staff, isactive, date_joined, first_name
#
#
class Usuario(AbstractUser):
    cidade = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)


def __str__(self):
        return f"Receita [nome={self.nome}]"