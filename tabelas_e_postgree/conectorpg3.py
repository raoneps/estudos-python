import psycopg2 as bd
import pandas as pd

from IPython.display import display

connection = bd.connect(
    database='dbtest',
    host='127.0.0.1',
    port='5432',
    user='postgres',
    password='admin')

cursor = connection.cursor()



print("Conectado com êxito! ")

sqlQuery = 'SELECT * FROM userteste' 

createUserTable = 'CREATE TABLE IF NOT EXISTS userteste (id serial primary key not null, first_name varchar(100) not null, last_name varchar(100) not null, email varchar(255) unique not null, created_at timestamp not null);'

insertInUser = "INSERT INTO userteste (id, first_name, last_name, email, created_at) VALUES (1, 'Raone', 'Silva', 'raone@teste.com', '2023-06-01 16:55:00');"

def create_table(sql):
  con = connection
  cur = con.cursor()
  cur.execute(sql)
  con.commit()


def consulta_db(sql):
  con = connection
  cur = con.cursor()
  cur.execute(sql)
  con.commit() 
  recset = cur.fetchall()
  registros = []
  for rec in recset:
    registros.append(rec)
  con.close()
  return registros

#def insert_inUser(sql):
#  con = connection
#  cur = con.cursor()
#  cur.execute(sql)
#  con.commit() 

create_table(createUserTable)
#insert_inUser(insertInUser)

reg = consulta_db(sqlQuery)

df = pd.DataFrame(reg)


print('\n', df)
display (df)
