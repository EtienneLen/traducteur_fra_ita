import sqlite3
import csv

conn = sqlite3.connect('itafra.db')

c = conn.cursor()

c.execute('create table fra_ita (id_fr INTEGER, trad_fr TEXT, id_ita INTEGER, trad_ita TEXT)')





conn.commit()
conn.close()