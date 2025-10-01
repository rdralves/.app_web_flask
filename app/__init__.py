from flask import Flask
from .models import db  # importa o db do seu models.py
from flask_login import LoginManager


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

    # Inicializa o banco
    db.init_app(app)

    # Registra blueprint
    from .routes import main_bp
    app.register_blueprint(main_bp)

    # Cria as tabelas
    with app.app_context():
        db.create_all()

    return app
