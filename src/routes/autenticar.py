from app import app, db
from flask import render_template, request, redirect, url_for, session, flash
from models import *

def user():
    if 'user' not in session or session['user'] == None:
        user = None
    else:
        user = Cadastro.query.filter_by(user_id=session['user']).first()
    return user

@app.route('/cadastrar', methods=["POST"])
def cadastrar():

    nomeCompleto = request.form["Nome"]
    sobrenome = request.form["Sobrenome"]
    usuario = request.form["Usuario"]
    email = request.form["Email"]
    senha = request.form["Senha"]
    confSenha = request.form["confSenha"]
    bairro = request.form["Bairro"]
    rua = request.form["Rua"]
    estado = request.form["Estado"]
    cep = request.form["cep"]
    cidade = request.form["Cidade"]

    if Cadastro.query.filter_by(user_email=email).first():
        flash("O email inserido já foi cadastrado!")
        return redirect(url_for('cadastro'))
    
    elif Cadastro.query.filter_by(user_usuario=usuario).first():
        flash("O usúario inserido já existe!")
        return redirect(url_for('cadastro'))
    
    elif senha != confSenha:
        flash("A senha e o confirmar senha não estão iguais")
        return redirect(url_for('cadastro'))
    
    else:
        novoUsuario = Cadastro (user_nome=nomeCompleto, user_sobrenome=sobrenome, user_email=email, user_senha=senha, user_confSenha=confSenha, user_usuario=usuario, user_bairro=bairro, user_rua=rua, user_estado=estado, user_cep=cep, user_cidade=cidade)
    
        db.session.add(novoUsuario)
        db.session.commit()

        session['user'] = novoUsuario.user_id
    
        return redirect(url_for('index'))

@app.route('/logar', methods=["POST"])
def logar():

    email = request.form['Email']
    senha = request.form['Senha']

    if not Cadastro.query.filter_by(user_email=email).first():
        flash('Email inexistente')
        return redirect(url_for('login'))
    
    elif Cadastro.query.filter_by(user_email=email).first().user_senha != senha:
        flash('Senha incorreta')
        return redirect(url_for('login'))
    
    else:
        session['user'] = Cadastro.query.filter_by(user_email=email).first().user_id
        return redirect(url_for('index'))
    
@app.route('/logout')
def logout():
    session['user'] = None

    return redirect(url_for('index'))

@app.route('/pagar', methods=["POST", "GET"])
def pagar():

    nome = request.form['Nome2']
    sobrenome = request.form['Sobrenome2']
    email = request.form['Email2']
    nomeCartao = request.form['cartaoNome']
    numeroCartao = request.form['cartaoNumero']
    cvv = request.form['CVV']

    if len(cvv) > 3:
        flash('Insira apenas 3 digitos!')
        return redirect(url_for('checkout'))

    novoPagamento = Pagamento(user_nome=nome, user_sobrenome=sobrenome, user_email=email, user_nomeCartao=nomeCartao, user_numeroCartao=numeroCartao, user_cvv=cvv)

    db.session.add(novoPagamento)
    db.session.commit()

    session['pagamento'] = novoPagamento.user2_id

    return redirect(url_for('pagamentoAprovado'))

