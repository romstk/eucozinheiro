from django.shortcuts import render, redirect
from usuarios.forms import CadastroForms, LoginForms, UpdatePasswordForms
from django.contrib.auth.models import User
from django.contrib import auth, messages


# views da aplicação usuários 
def login(request): 
    #instacia da classe LoginFrom
    form = LoginForms()

    if request.method == "POST":
        #puxando os dados do formulário postado para uma variável.
        form = LoginForms(request.POST)

        #validando o formulário
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        #neste ponto faremos a validação do usuário passando para um método do Django que fará a autenticação    

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
       #se o usuário for válido passo os parâmetros request e o usuário que vamos autenticar
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, "usuário logado!")
            return redirect('home')
        else:
            messages.error(request, "Erro ao efetuar login!")
            return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})

def logout(request):
    auth.logout(request)
    messages.info(request, "Logout efetuado!")
    return redirect('login')

def cadastro(request):
    #instancia de forms 
    form = CadastroForms()
    
    #testamos qual o método fez a chamada para a view para tratarmos a ação cfe o método 
    if request.method == "POST":
        #armazeno os dados do formulário enviados por post na variável form
        #instancia de forms 
        form = CadastroForms(request.POST)

        if form.is_valid():
            #se senha e confirma senha não forem iguais vai apresentar mensagem de erro
            if form['senha_1'].value () != form['senha_2'].value(): 
                messages.error(request, "Senha e confirmação devem ser iguais")
                return redirect('cadastro')
            #atribuindo as variáveis com dados dos campos do forms.
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            #vamos testar agora se o usuário a ser cadastrado já existe, se existir redireciona para a página de cadastro novamente para cadastrar novo usuário
            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuário já existente. Modifique o nome do usuário e tente novo cadastramento.")
                return redirect('cadastro')
            
            #após todas as validações crio um novo usuário de fato
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Usuário cadastrado com sucesso! Você já pode fazer o login, ")
            return redirect('login')
    #este return vai ser chamado somente se o método do request for diferente de POST, ou seja, se o formulário for chamado para cadastrar novo usuário     
    #ao renderizar o template passamos um dicionário com o form instanciado para apresentar os fields em tela 
    return render(request, 'usuarios/cadastro.html', {"form": form })


def update_password_user(request):
    #instancia de forms 
    form = UpdatePasswordForms()

    if request.method == 'POST':
        #puxando os dados do formulário postado para uma variável.
        form = UpdatePasswordForms(request.POST)
        #validando o formulário
        if form.is_valid():
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha'].value()
            #neste ponto vou testar se usuário existe. 
            #se existir vai atribuir a variavel usuario os dados do usuario que recebemos os dados por post para alterar a senha.             
            if not User.objects.filter(username=nome).exists():
               messages.error(request, 'Usuário invalido')
               return redirect('update_password_user')
            usuario = User.objects.get(username=nome)
            #Encontrando o usuário então testamos se o email é válido 
            if usuario.email != email:
                messages.error(request, 'Email informado é invalido')     
                return redirect('update_password_user')
            
            #Se todos os testes foram atendidos positivamente vamos fazer o update da senha
            usuario.set_password(senha)
            usuario.save()
            messages.success(request, 'Dados informados estão corretos. Senha atualizada. ')
            return redirect('login')
                
                

    return render(request, 'usuarios/update_password.html', {"form": form })