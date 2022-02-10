import sqlite3
import csv
import random


answer = random.randint(0,3)

alea = []
for i in range(4) :
    alea.append(random.randint(1,70000))



conn = sqlite3.connect('itafra.db')
c = conn.cursor()
#This query selects multiple id that are randomly generated
c.execute("SELECT rowid, * FROM fra_ita WHERE rowid IN (?,?,?,?)", (alea))
req1 = c.fetchall()
conn.commit()
conn.close()

print('--- --- --- ---')
print('Quelle est la traduction de la phrase suivante ? ')
print('--- --- --- ---')
print(req1[answer][2])


def user_choice() :
    iteration = 1
    for req in req1 :
        print('--- --- --- ---')
        print(f"{iteration} ) {req[4]}")
        iteration =iteration + 1

def correction() :
    user_answer = int(input("Votre réponse : "))-1
    if (user_answer == answer) :
        print("Bonne réponse")
    else :
        print('Mauvaise réponse')

def get_query_all() :
    return req1

user_choice()
correction()
