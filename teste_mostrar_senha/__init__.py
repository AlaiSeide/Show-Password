from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f082cf647f7acfd17fd73591f75660e5' 

# localhost de Bötelkamp
localhost =  '192.168.56.1'

# Configuração da conexão com o banco de dados MySQL no XAMPP
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:flashreverso20@{localhost}/loginpage'

# Criação de um objeto SQLAlchemy e associação à instância do Flask (app)
# SQLAlchemy é uma biblioteca para trabalhar com bancos de dados relacionais de forma orientada a objetos
# Associar o objeto SQLAlchemy à instância do Flask permite usar recursos do SQLAlchemy na aplicação Flask
database = SQLAlchemy(app)
login_manager = LoginManager(app)
# a pagina onde o usuario sera redirecionado caso tente acessar uma pagina sem fazer login
# passei login que é a minha pagina de cadastro
login_manager.login_view = 'home'
login_manager.login_message = 'Faça login para acessar esta página, por favor.'
login_manager.login_message_category = 'alert-info'

from teste_mostrar_senha import routes

