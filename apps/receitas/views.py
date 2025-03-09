from django.shortcuts import get_object_or_404, render, redirect
from apps.receitas.models import Receita
from django.contrib import messages
from apps.receitas.forms import ReceitaForms



def index (request):
    #criando um objeto que vai trazer os dados do banco de dados através de models.
    #Filtramos apenas as receitas publicadas e ordenando por data 
    receitas = Receita.objects.order_by("data").filter(publicada=True)
    return render(request, 'receitas/index.html', {"cards" : receitas})

def termos_uso(request):
    return render(request, 'termos_uso.html')

def politica_privacidade(request):
    return render(request, 'politica_privacidade.html')
#recebe os dados do formulário de pesquisa trazendo do formulário o dado que deverá ser pesquisado para filtrar por nome as receitas que contenham o filtro pesquisado. Se o filtro vier vazio vai mostrar todas as receitas. 
def filtro(request):
    if request.method == "POST": 
        filtro = request.POST.get('filtro')
        if filtro:
            receitas = Receita.objects.order_by("data").filter(publicada=True, nome__icontains=filtro)
        else: 
            receitas = Receita.objects.order_by("data").filter(publicada=True)

        
        return render(request, 'receitas/index.html#receitas__container', {"cards" : receitas})        

#Esta function tem o nome da url definida em urls.py(rlpatterns), ao ser chamada a url aciona esta função
def receita(request, receita_id): 
    #primeiramente vamos testar se o usuário está logado. Se não tiver vamos redirecionar para login
    if not request.user.is_authenticated:
        messages.error(request, "Usuário deve estar logado para acessar a receita. ")
        return redirect('login')
    #Vamos capturar o objeto do banco de dados com base no id(pk-->primary key)recebida pela url
    receita = get_object_or_404(Receita , pk=receita_id)
    #Ao renderizar passo além da url um dicionário com os dados da receita
    return render(request, 'receitas/receita.html', {"receita": receita})


def nova_receita(request):
    #primeiramente vamos testar se o usuário está logado. Se não tiver vamos redirecionar para login
    if not request.user.is_authenticated:
        messages.error(request, "Usuário deve estar logado para acessar esta funcionalidade")
        return redirect('login')
    
    #se o método for GET vai pular para última linha, levando para o form de inclusão de nova receita
    form = ReceitaForms()
    if request.method == 'POST': 
        form = ReceitaForms(request.POST, request.FILES)

        if form.is_valid():
            #neste ponto depois de tudo validado vamos atribuir o usuário logado ao registro que será salvo.
            # Obtém o usuário logado
            usuario = request.user 

            # Adiciona os dados do usuário ao formulário
            form.instance.autor_id = usuario.id  # Usuario, o campo que é a ForeignKey

            form.save() #como estamos usando um ModelForm-FotografiaForm já basta mandar o form ser salvo que o Django se encarrega de tratar a model vinculada ao form e salvar os dados. 
            messages.success(request, 'Receita cadastrada')
            return redirect('home') 
    #se o método for GET vai pular para última linha, levando para o form de inclusão de nova receita
    return render(request, 'receitas/nova_receita.html', {'form': form} )
    
    
#recebemos da urls.py o receita_id passado na url para processar a requisição através do request
def editar_receita(request, receita_id):
    #aqui faço a busca da receita pelo id
    receita = Receita.objects.get(id=receita_id)
     #aqui estou criando uma instancia de do formulário passando os dados da receita localizada no banco de dados 
    form = ReceitaForms(instance=receita)

    if request.method == 'POST': 
        #se receber os dados por post vai capturar os novos dados recebidos e instance significa que o que não for mudado ele pega de receita já instanciada para fazer o update. 
        form = ReceitaForms(request.POST, request.FILES, instance=receita)
        if form.is_valid():
            form.instance.publicada = False
            form.save()#como estamos usando um ModelForm-ReceitaForm já basta mandar o form ser salvo que o Django se encarrega de tratar a model vinculada ao form e salvar os dados. 
            messages.success(request, 'Receita editada.')
            return redirect(f'/receita/{receita_id}/')
    return render(request, 'receitas/editar_receita.html', {'form':form, 'receita_id': receita_id })

#recebemos da urls.py o receita_id passado na url para processar a requisição através do request
def deletar_receita(request, receita_id):
        #aqui faço a busca da fotografia pelo id
        receita = Receita.objects.get(id=receita_id)
        #se o usuário não estiver logado ou não for o proprietário não poderá deletar 
        if not (request.user.is_authenticated) or not (receita.autor_id == request.user.id): 
            messages.error(request, "Para apagar receita tem que estar logado e ser o propritário. ")
            return redirect('login')
        receita.delete()
        messages.success(request, 'Receita apagada.')
        return redirect('home')
    

#Recebe o id da receita e manipula o campo publicada. Se estiver True vai editar para False, se estiver False vai editar para True
def publicar_receita(request, receita_id):
    receita = Receita.objects.get(id=receita_id)
    publicada = receita.publicada
    #Seta o novo status invertendo o atual
    publicada = not publicada
    receita.publicada = publicada
    receita.save()
    messages.success(request, 'Status de publicação editado com sucesso! ')
    return redirect(f'/receita/{receita_id}/')



#esta função vai listar as receitas para o usuário admin(superusuario) pois com a lista poderá visualizar todas as receitas, filtrar, e mudar status de publicada para True ou False.
def lista_receitas(request, filtro): 
    if not (request.user.is_authenticated): 
            messages.error(request, "Acesso a esta funcionalidade somente para usuários logadps. ")
            return redirect('login')
    
    #Essa linha faz a conversão. Primeiro, ela converte a string filtro para minúsculas (.lower()) para lidar com variações como 'True', 'TRUE' ou 'true'. Em seguida, ela compara a string em minúsculas com 'true'. O resultado dessa comparação é um booleano (True ou False), que é atribuído à variável filtro.
    filtro = filtro.lower() == 'true'   
    
    #Se o usuário logado for superusuário fará um filtro para todas as mensagens
    if (request.user.is_superuser): 
        if filtro:    
            #Se filtro for True - mostra as receitas publicadas 
            receitas = Receita.objects.order_by("data").filter(publicada=bool(filtro))        
        else:
            #Se filtro for False - mostra as receitas ainda não publicadas 
            receitas = Receita.objects.order_by("data").filter(publicada=bool(filtro))
    #Se o usuário não for superusuário vai buscar as mensagens somente de sua propriedade 
    if not (request.user.is_superuser): 
        if filtro:    
            #Se filtro for True - mostra as receitas publicadas 
            receitas = Receita.objects.order_by("data").filter(publicada=bool(filtro), autor=request.user)        
        else:
            #Se filtro for False - mostra as receitas ainda não publicadas 
            receitas = Receita.objects.order_by("data").filter(publicada=bool(filtro), autor=request.user)

    return render(request, 'receitas/lista_receitas.html', {"cards" : receitas})