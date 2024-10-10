#Arquivo usado somente para rodar a aplicação no servidor na web
# Este arquivo inicia a aplicação chamando os arquivos de configuração e o manege.py para rodar a app

import sys
import os

# Adiciona o caminho da aplicação ao sys.path
sys.path.insert(0, '/var/www/html/eucozinheiro')

# Ajusta a variável de ambiente se necessário
os.environ['PYTHON_EUCOZINHEIRO_SETTINGS'] = '/var/www/html/eucozinheiro/manage.py'

# Importa a aplicação do seu framework web (por exemplo, Django)
from setup.wsgi import application 