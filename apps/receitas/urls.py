#Arquivo responsável pelo gerenciamento das urls específicas da app receitas que será #importado no urls.py do setup da aplicação geral 
# importamos aqui as views de receitas para poder utilizá-las na lista de rotas/urls

from django.urls import path
from apps.receitas.views import index, filtro, receita, nova_receita, editar_receita, deletar_receita, lista_receitas, publicar_receita

#Criamos uma lista que será responsável por gerenciar as rotas/urls do app galeria
urlpatterns = [
        path('', index, name='home'),
        path('receita/<int:receita_id>/', receita, name='receita'),
        path('nova-receita', nova_receita, name='nova_receita'),
        path('editar-receita/<int:receita_id>', editar_receita, name='editar_receita'),
        path('deletar-receita/<int:receita_id>', deletar_receita, name='deletar_receita'),
        path('filtro', filtro, name='filtro'),
        path('lista-receitas/<str:filtro>', lista_receitas, name='lista_receitas'),
        path('publicar-receita/<int:receita_id>', publicar_receita, name='publicar_receita'),

]

