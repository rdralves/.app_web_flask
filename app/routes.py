from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Usuario, db

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
def index():
    hello = "Hello _Flask!"
    return render_template('index.html', hello=hello)


@main_bp.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        data_nascimento = request.form.get('data_nascimento')

        if not name or not email or not password or not data_nascimento:
            flash("Todos os campos são obrigatórios.", "warning")
            return render_template('cadastro.html')

        password_hash = generate_password_hash(password)

        try:
            if Usuario.query.filter_by(email=email).first():
                flash("Erro: Email já cadastrado.", "danger")
            else:
                novo_usuario = Usuario(
                    nome=name, email=email, senha_hash=password_hash, data_nascimento=data_nascimento)
                db.session.add(novo_usuario)
                db.session.commit()

                flash(f"Usuário {name} salvo com sucesso!", "success")
                return redirect(url_for('main_bp.login'))
        except Exception as e:
            print(f"Erro ao salvar usuário: {e}")
            flash("Erro interno ao salvar usuário.", "danger")

    return render_template('cadastro.html')


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash("Todos os campos são obrigatórios.", "warning")
            return render_template('login.html')

        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and check_password_hash(usuario.senha_hash, password):
            login_user(usuario)
            flash(f"Bem-vindo de volta, {usuario.nome}!", "success")
            return redirect(url_for('main_bp.dashboard'))
        else:
            flash("Email ou senha inválidos.", "danger")

    return render_template('login.html')


@main_bp.route('/dashboard')
@login_required
def dashboard():
    dados = Usuario.query.all()
    return render_template('dashboard.html', dados=dados)


@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Você foi desconectado com sucesso.", "success")
    return redirect(url_for('main_bp.login'))
