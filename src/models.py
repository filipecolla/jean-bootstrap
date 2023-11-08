from app import db
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.sql import func

class Cadastro(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_nome = db.Column(db.String, nullable=False)
    user_sobrenome = db.Column(db.String, nullable=False)
    user_usuario = db.Column(db.String, nullable=False)
    user_email = db.Column(db.String, nullable=False)
    user_senha = db.Column(db.String, nullable=False)
    user_confSenha = db.Column(db.String, nullable=False)
    user_bairro = db.Column(db.String, nullable=True)
    user_rua = db.Column(db.String, nullable=True)
    user_cep = db.Column(db.Integer, nullable=True)
    user_estado = db.Column(db.String, nullable=False)
    user_cidade = db.Column(db.String, nullable=False)

class Pagamento(db.Model):
    user2_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_nome = db.Column(db.String, nullable=False)
    user_sobrenome = db.Column(db.String, nullable=False)
    user_email = db.Column(db.Text, nullable=False)
    user_nomeCartao = db.Column(db.Integer, nullable=False)
    user_numeroCartao = db.Column(db.Integer, nullable=False)
    user_cvv = db.Column(db.Integer, nullable=False)