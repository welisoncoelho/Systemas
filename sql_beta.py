import pandas as pd
import sqlite3
import psycopg2 as pg
from sqlalchemy import create_engine


# Criando o Conn
host = 'localhost'
user = 'postgres'
password ='Xurupit@'
sslmode ='require'

#srintgconexão
#engine= create_engine('postgresql://postgres:Xurupit@localhost:5432/Ad_sistema')
connection= pg.connect(user ='postgres',password = "Xurupit@", host="localhost",port='5432',database='Ad_sistema')

df_adv = pd.read_sql("SELECT * FROM advogados", connection)
df_proc =pd.read_sql("SELECT * FROM processos", connection)

connection.commit()
connection.close()




