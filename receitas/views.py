from django.shortcuts import render, get_object_or_404
from receitas.models import Receita


def index (request):
    #criando um objeto que vai trazer os dados do banco de dados através de models.
    #Filtramos apenas as receitas publicadas e ordenando por data 
    receitas = Receita.objects.order_by("data").filter(publicada=True)
    return render(request, 'receitas/index.html', {"cards" : receitas})


#Esta function tem o nome da url definida em urls.py(rlpatterns), ao ser chamada a url aciona esta função
def receita(request, receita_id): 
    #Vamos capturar o objeto do banco de dados com base no id(pk-->primary key)recebida pela url
    receita = get_object_or_404(Receita , pk=receita_id)
    #Ao renderizar passo além da url um dicionário com os dados da receita
    return render(request, 'receitas/receita.html', {"receita": receita})
