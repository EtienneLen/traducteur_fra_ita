from flask import Flask, render_template
import sqlite3
import datas.utils
import random


app = Flask(__name__)
FLASK_DEBUG = 1


@app.route('/')
def root():
    answer = random.randint(0,3)

    alea = []
    for i in range(4) :
        alea.append(random.randint(1,70000))

    conn = sqlite3.connect('itafra.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM fra_ita WHERE rowid IN (?,?,?,?)", (alea))
    req1 = c.fetchall()
    conn.commit()
    conn.close()
    

    return render_template('index.html', requete=str(req1[3][2]) + "-" + str(req1[3][4]))






