import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mned2003@',
    database='bdacademia',
)
cursor = conexao.cursor()






cursor.close()
conexao.close()