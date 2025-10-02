from flask import Flask
from .models import Usuario, db  # importa o db do seu models.py
from flask_login import LoginManager
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)

    # Configurações
    app.config['SECRET_KEY'] = 'your_secret_key'
    # ou outro banco como PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastro.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configuração do Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'main_bp.login'  # 👈 define a rota de login

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))  # 👈 busca o usuário pelo ID

    # Inicializa o banco
    db.init_app(app)
    migrate = Migrate(app, db)  # Inicializa o Flask-Migrate
    # Registra blueprint
    from .routes import main_bp
    app.register_blueprint(main_bp)

    # Cria as tabelas
    with app.app_context():
        db.create_all()

    return app
