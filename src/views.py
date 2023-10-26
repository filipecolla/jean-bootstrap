from flask import render_template, request, redirect, flash, url_for, session
from app import app, db
from models import Cadastro, Pagamento
from sqlalchemy import union

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/comprar')
def comprar():
    return render_template('comprar.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')