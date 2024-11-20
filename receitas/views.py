from django.shortcuts import render


def index (request):
    return render(request, 'receitas/index.html')


#Esta function tem o nome da url definida em urls.py(rlpatterns), ao ser chamada a url aciona esta função
def receita(request): 
    return render(request, 'receitas/receita.html')