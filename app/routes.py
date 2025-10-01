from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from app.models import Usuario, db

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
def index():
    hello = "Hello, World! Hello _Flask!"
    return render_template('index.html', hello=hello)


@main_bp.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if not name or not email or not password:
            flash("Todos os campos são obrigatórios.", "warning")
            return render_template('cadastro.html')

        password_hash = generate_password_hash(password)

        try:
            if Usuario.query.filter_by(email=email).first():
                flash("Erro: Email já cadastrado.", "danger")
            else:
                novo_usuario = Usuario(
                    nome=name, email=email, senha_hash=password_hash)
                db.session.add(novo_usuario)
                db.session.commit()

                flash(f"Usuário {name} salvo com sucesso!", "success")
                return redirect(url_for('main_bp.index'))
        except Exception as e:
            print(f"Erro ao salvar usuário: {e}")
            flash("Erro interno ao salvar usuário.", "danger")

    return render_template('cadastro.html')
# update_routes