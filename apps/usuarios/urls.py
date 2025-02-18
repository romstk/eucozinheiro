from django.urls import path
from apps.usuarios.views import cadastro,login, logout, update_password_user

#Neste arquivo vamos criar as rotas/urls para as views da aplicação usuários. 
urlpatterns = [
        path('cadastro', cadastro, name='cadastro'),
        path('login', login, name='login'),
        path('logout', logout, name='logout'),
        path('update_password_user', update_password_user, name='update_password_user')
]