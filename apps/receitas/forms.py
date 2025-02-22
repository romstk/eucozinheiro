#Classe responsável por gerenciar os formulários da aplicação de receitas
from django import forms
from apps.receitas.models import Receita
from django import forms

class ReceitaForms(forms.ModelForm):
    #Dentro desta classe de formulário vou inserir outra classe com os matadados da model que irei utilizar para criar o form
    class Meta:
        model = Receita
        exclude = ['autor', 'data', 'publicada',] #este atributo refere-se aos fields da model que não quero incluir no formulário
        labels = {
            'nome' : "Nome",
            'descricao' : "Descrição",
            'ingredientes' : "Ingredientes", 
            'preparo' : "Mode de Preparo",
            'imagem' : "Foto do Prato:  Recomendado uma foto tamanho: 800px X 800Ppx máximo 200kb"
        }

        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control'}),
            'descricao' : forms.TextInput(attrs={'class': 'form-control'}),
            'ingredientes' : forms.Textarea(attrs={'class' : 'form-control'}),
            'preparo' : forms.Textarea(attrs={'class' : 'form-control'}),
            'imagem' : forms.FileInput(attrs={'class' : 'form-control'}),
        }

    #Este método faz a validação do tamanho da imagem máxima aceita no formulário e retorna um erro caso a imagem não possa ser aceita 
    def clean_imagem(self):
        tamanho_maximo = 200 * 1024 #variável que define o tamanho máximo de arquivo que podemos fazer o upload transformando em kbytes
        arquivo = self.cleaned_data.get('imagem')  #'arquivo' é o nome do campo FileField no seu formulário
        
        if arquivo is not None and arquivo.size > tamanho_maximo: 
                raise forms.ValidationError(f"Tamanho do arquivo não pode exceder {tamanho_maximo / 1024} KB")
        else: 
            return arquivo        