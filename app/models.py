import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin  # 👈 Importa o mixin necessário
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Usuario(db.Model, UserMixin):  # 👈 Herda de UserMixin
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(200), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)  
    data_registro = db.Column(
        db.DateTime, default=datetime.utcnow)  


    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)
