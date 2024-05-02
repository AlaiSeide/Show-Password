from teste_mostrar_senha import app, database
from flask import render_template, url_for, redirect
from teste_mostrar_senha.forms import LoginForm, CriarContaForm
from teste_mostrar_senha.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
           # Então, resumindo, essa linha de código está procurando no banco de dados pelo usuário que possui o email fornecido no formulário de login e armazenando esse usuário na variável usuario.
            usuario = Usuario.query.filter_by(email=form.email.data).first()
            #print(usuario.senha)
            # se o usuario existe e se a senha que ele preencheu é a mesma que ta no banco de dados
            if usuario and usuario.senha == form.senha.data:
                 login_user(usuario)
                 return redirect(url_for('homepage'))
            else:
                 return redirect(url_for('criar_conta'))
    return render_template('home.html', form=form)

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/criar-conta', methods=['GET', 'POST'])
def criar_conta():
    formcriarconta = CriarContaForm()

    if formcriarconta.validate_on_submit():
        usuario = Usuario(username=formcriarconta.username.data, email=formcriarconta.email.data, senha=formcriarconta.senha.data)
        database.session.add(usuario)
        database.session.commit()
        return redirect(url_for('homepage'))
    return render_template('criar_conta.html', formcriarconta=formcriarconta)