from django.shortcuts import render
from receitas.models import Receita


def index (request):
    #criando um objeto que vai trazer os dados do banco de dados através de models.
    receitas = Receita.objects.all()
    return render(request, 'receitas/index.html', {"cards" : receitas})


#Esta function tem o nome da url definida em urls.py(rlpatterns), ao ser chamada a url aciona esta função
def receita(request): 
    return render(request, 'receitas/receita.html')