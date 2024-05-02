from teste_mostrar_senha import database, login_manager
from flask_login import UserMixin

# encontrar o usuario apartir de um id
@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), nullable=False)
    email = database.Column(database.String(120), nullable=False, unique=True)
    senha = database.Column(database.String(80), nullable=False)