from django.contrib import admin

from apps.receitas.models import Receita


class ListandoReceitas(admin.ModelAdmin):
    #propriedade que definine como os registros serão exibidos, quais propriedades mostrar na lista
    list_display = ("id", "nome", "descricao")
    #quais propriedades conterão link para acessar o registro
    list_display_links = ("id", "nome")
    #Campo para pesquisa por nome na listagem de receitas 
    search_fields = ("nome",)
    #Campo para filtro personalizado pelo campo publicada para filtrar as receitas 
    list_filter = ("publicada",)
    #define a quantidade de registros por página na listagem 
    list_per_page = 20 

# Register your models here.
# Com o import de Receita e o comando de registro teremos acesso ao model(dados) diretamente no DjnagoAdmin via navegador 
admin.site.register(Receita, ListandoReceitas)
