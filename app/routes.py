from flask import Blueprint, render_template, request
from werkzeug.security import generate_password_hash
from app.models import Usuario, db
main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/', methods=['GET', 'POST'])
def home():
    hello = "Hello, World! Hello _Flask!"
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        password_hash = generate_password_hash(password)

        print(f"Name: {name}, Email: {email}")

        try:
            if Usuario.query.filter_by(email=email).first():
                print("Erro: Email já cadastrado.")
            else:
                # Cria o usuário e salva no banco
                novo_usuario = Usuario(
                    nome=name, email=email, senha_hash=password_hash)
                # novo_usuario.set_senha(password)
                db.session.add(novo_usuario)
                db.session.commit()

                print(f"Usuário {name} salvo com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar usuário: {e}")

    return render_template('index.html', hello=hello)
