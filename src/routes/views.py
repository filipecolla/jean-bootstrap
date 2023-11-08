from flask import render_template, request, redirect, flash, url_for, session
from app import app, db
from models import Cadastro, Pagamento
from sqlalchemy import union

def user():
    if 'user' not in session or session['user'] == None:
        user = None
    else:
        user = Cadastro.query.filter_by(user_id=session['user']).first()
    return user

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', user = user())

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', user = user())

@app.route('/comprar')
def comprar():
    return render_template('comprar.html', user = user())

@app.route('/checkout')
def checkout():
    return render_template('checkout.html', user = user())

@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    return render_template('cadastro.html', user = user())

@app.route('/cadastroFeito')
def cadastroFeito():
    return render_template('cadastroFeito.html', user = user())

@app.route('/users', methods=["GET", "POST"])
def userCadastrados():

    filtro = Cadastro.query.all()

    filtro = list(reversed(filtro))

    return render_template('userCadastrados.html', user = user(), usuarios=filtro)

@app.route('/pagamentoAprovado')
def pagamentoAprovado():
    
    pagamento = Pagamento.query.all()

    return render_template('pagamentoAprovado.html', user = user(), pagamentosAprovado=pagamento)

@app.route('/login', methods=["POST", "GET"])
def login():
    if user() != None:
        return redirect(url_for('index'))
    return render_template('login.html', user = user())