# import secrets

# secrec_key = secrets.token_hex(16)
# #print(secrec_key)

# from teste_mostrar_senha import app

# #print(app.root_path)

from teste_mostrar_senha import app, database
from teste_mostrar_senha.models import Usuario

with app.app_context():
    database.create_all()