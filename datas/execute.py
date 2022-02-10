import sqlite3
import csv

id_debut = int(input("Saissez l'id de début : "))

conn = sqlite3.connect('itafra.db')
c = conn.cursor()
c.execute("SELECT rowid, * FROM fra_ita WHERE rowid > ? LIMIT 10", (id_debut,))
req1 = c.fetchall()
conn.commit()
conn.close()

for req in req1 :
    print(req[2])
    print(req[4])
    print('---- ---- ---- ----')


