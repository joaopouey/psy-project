import sqlite3

from flask import Flask, session, redirect, render_template, request
from flask_session import Session

from helpers import login_required


# Create and execute a Flask app
app = Flask(__name__)

# Open psi.db and create a cursor
con = sqlite3.connect('psi.db')
cur = con.cursor()

#Configure Session
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    # Esquecer user_id conectado.
    session.clear()

    # Caso o usuário envie um formulário por GET (clicando em um link ou sendo redirecionado)
    if request.method == "GET":
        return render_template("login.html")
    
    # Caso o usuário envie um formulário via POST (tentando fazer o login)
    else:
        return ('TODO')




con.close()

