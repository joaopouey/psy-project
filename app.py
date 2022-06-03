from itertools import count
import sqlite3
from flask import Flask, session, redirect, render_template, request
from flask_session import Session
from helpers import login_required



# Create and execute a Flask app
app = Flask(__name__)

# Connect to database (psi.db)
con = sqlite3.connect('psi.db', check_same_thread=False)
cur = con.cursor()

#Configure Session
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    # Esquecer user_id conectado.
    session.clear()

    # Caso o usuário envie um formulário por GET (clicando em um link ou sendo redirecionado).
    if request.method == "GET":
        return render_template("login.html")
    
    # Caso o usuário envie um formulário via POST (tentando fazer o login).
    else:
        # Buscar username no banco de dados.
        
        user_search = cur.execute("SELECT id FROM usuarios WHERE nome = ?;", [request.form.get("username")])
        if len(user_search) != 1:
            return ('Usuário não encontrado')
        else:
            return ('kkkkkkk')

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/fechamento")
def fechamento():
    return render_template("fechamento.html")




