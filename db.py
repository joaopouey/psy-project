import sqlite3

con = sqlite3.connect('psi.db')
cur = con.cursor()


# db.execute ('''CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome TEXT NOT NULL, valor INTEGER NOT NULL)''')
# db.execute ('''CREATE TABLE consultas(id INTEGER, dias TEXT, nr_consultas INTEGER, total INTEGER, FOREIGN KEY (id) REFERENCES usuarios(id))''')


con.commit()
con.close()
