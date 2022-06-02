from flask import Flask, session
from flask_session import Session
import sqlite3

# Create and execute a Flask app
app = Flask(__name__)

# Open psi.db and create a cursor
con = sqlite3.connect('psi.db')
cur = con.cursor()

#Configure Session
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")





con.close()

