#Classe responsável por gerenciar os formulários da aplicação de usuários 
from django import forms

class LoginForms(forms.Form): 
    nome_login = forms.CharField(
        label = "Nome Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "col-6 form-control",
                "placeholder": "Informe nome de usuário cadastrado"
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "col-4 form-control",
                "placeholder" : "Digite sua senha"
            }
        )

    )



class CadastroForms(forms.Form):

    nome_cadastro = forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "col-6 form-control",
                "placeholder": "Nome. Informar nome sem espaços. Será usado para o acesso ao site. Ex. josesilva"
            }
        )
    )

    email = forms.EmailField(
        label="Email", 
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "col-5 form-control",
                "placeholder": "Ex. josesilva@gmail.com"
            }
        )
    )

    senha_1 = forms.CharField(
        label = "Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "col-4 form-control",
                "placeholder" : "Digite sua senha"
            }
        )
    )
    
    senha_2 = forms.CharField(
        label = "Confirme sua Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "col-4 form-control",
                "placeholder" : "Confirme sua senha"
            }
        )
    )
    


    #este método fará a validação do campo nome de cadastro. 
    #deve iniciar com clean_ e seguir com o nome do campo que quero validar para que o django entenda que é um método clean. O self como parâmetro significa que é desta classe, vai puxar as informações desta classe
    def clean_nome_cadastro(self):
        #vamos pegar do campo nome_cadastro passado pelo formulário após ser validado
        nome = self.cleaned_data.get("nome_cadastro")

        #se o nome tiver algum dado vai aplicar o método que tira os espaços das extremidades e transforma tudo em minúsculas 
        if nome:
            nome = nome.strip()
            #se nome tiver espaços vamos lançar uma mensagem de erro pois não poderá #aceitar nomes com espaços entre as palavras

            #raise.ValidateError é usado em formulários no Django para lançar um erro #de validação quando os dados fornecidos pelo usuário não atendem a #determinados critérios. Ele faz parte do sistema de validação do Django, #que é uma ferramenta poderosa #para garantir que os dados de entrada sejam #válidos antes de serem #processados.

            if " " in nome: 
                raise forms.ValidationError("Espaços não são permitidos neste campo.")
            else:
                return nome

    #faz a validação para testar se a senha e confirmação da senha são iguais e caso contrário apresenta mensagem de erro
    def clean_senha_2(self):
         senha_1 = self.cleaned_data.get("senha_1")
         senha_2 = self.cleaned_data.get("senha_2")

         if senha_1 and senha_2: 
              if senha_1 != senha_2:
                   raise forms.ValidationError("Sennha e confirmação de senha devem ser iguais.")
              else:
                   return senha_2


class UpdatePasswordForms(forms.Form):
    #Formulário utilizado para alteração da senha do usuário. 
    #O usuário precisa informar os campos do cadstro para o sistema aceitar a troca de senha.
    nome_cadastro = forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "col-6 form-control",
                "placeholder": "Nome. Informar o nome de usuário cadastrado"
            }
        )
    )

    email = forms.EmailField(
        label="Email", 
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "col-5 form-control",
                "placeholder": "Informar o email cadastrado"
            }
        )
    )

    senha = forms.CharField(
        label = "Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "col-4 form-control",
                "placeholder" : "Digite a nova senha"
            }
        )
    )