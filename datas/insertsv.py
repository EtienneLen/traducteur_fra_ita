import sqlite3
import csv

conn = sqlite3.connect('itafra.db')
c = conn.cursor()

file = open('corresp_ita_fra.tsv',encoding='UTF8')
contents = csv.reader(file, delimiter="\t")

c.executemany("INSERT INTO fra_ita (id_fr, trad_fr, id_ita, trad_ita) VALUES (?,?,?,?)",contents)


conn.commit()
conn.close()
