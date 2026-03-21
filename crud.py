import mysql.connector
from modelos import Aluno, Plano, Instrutor
from abc import ABC, abstractmethod
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mned2003@',
    database='bdacademia',
)
class Gerenciador(ABC):
    @abstractmethod
    def adicionando(self):
        pass
    @abstractmethod
    def listando(self):
        pass
    @abstractmethod
    def limpando(self):
        pass
    @abstractmethod
    def alterando(self):
        pass

class GerenciadorAluno(Gerenciador):
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = conexao.cursor()
    def adicionando(self, nome_aluno, email_aluno, telefone_aluno, cpf_aluno, id_plano):
        comando = 'INSERT INTO aluno (nome_aluno, email_aluno, telefone_aluno, cpf_aluno, id_plano) VALUES (%s, %s, %s, %s, %s)'
        self.cursor.execute(comando, (nome_aluno, email_aluno, telefone_aluno, cpf_aluno, id_plano))
        self.conexao.commit()
    def listando(self):
        comando = 'SELECT * FROM aluno'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() # ler o banco de dados
        for aluno in resultado:
            print(f"""
            ID: {aluno[0]}
            Nome: {aluno[1]}
            CPF: {aluno[2]}
            E-mail: {aluno[3]}
            Telefone: {aluno[4]}
            Plano ID: {aluno[5]}
            """)
    
    def limpando(self, nome_aluno):
        comando = 'DELETE FROM aluno WHERE nome_aluno = %s'
        self.cursor.execute(comando, (nome_aluno,))
        self.conexao.commit() #edita o banco de dados
    def alterando(self, nome, campo, valor_alterado):
        comando = f'UPDATE aluno SET {campo} = %s WHERE nome_aluno = %s'
        self.cursor.execute(comando, (valor_alterado, nome))
        self.conexao.commit()

class GerenciadorInstrutor(Gerenciador):
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = conexao.cursor()
    def adicionando(self, nome_instrutor, cpf_instrutor ,email_instrutor, telefone_instrutor, especialidade):
        comando = 'INSERT INTO instrutor (nome_instrutor, cpf_instrutor ,email_instrutor, telefone_instrutor, especialidade) VALUES (%s, %s, %s, %s, %s)'
        self.cursor.execute(comando, (nome_instrutor, cpf_instrutor ,email_instrutor, telefone_instrutor, especialidade))
        self.conexao.commit()
    def listando(self):
        comando = 'SELECT * FROM instrutor'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() # ler o banco de dados
        for instrutor in resultado:
            print(f"""
            ID: {instrutor[0]}
            Nome: {instrutor[1]}
            CPF: {instrutor[2]}
            E-mail: {instrutor[3]}
            Telefone: {instrutor[4]}
            Especialidade: {instrutor[5]}
            """)
    
    def limpando(self, nome_instrutor):
        comando = 'DELETE FROM instrutor WHERE nome_instrutor = %s'
        self.cursor.execute(comando, (nome_instrutor,))
        self.conexao.commit() #edita o banco de dados
    def alterando(self, nome, campo, valor_alterado):
        comando = f'UPDATE instrutor SET {campo} = %s WHERE nome_instrutor = %s'
        self.cursor.execute(comando, (valor_alterado, nome))
        self.conexao.commit()

class GerenciadorPlano(Gerenciador):
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = conexao.cursor()
    def adicionando(self, nome_plano, preco_plano, vantagens, desvantagens):
        comando = 'INSERT INTO plano (nome_plano,  preco_plano, vantagens, desvantagens) VALUES (%s, %s, %s, %s)'
        self.cursor.execute(comando, (nome_plano, preco_plano, vantagens, desvantagens))
        self.conexao.commit()
    def listando(self):
        comando = 'SELECT * FROM plano'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() # ler o banco de dados
        for plano in resultado:
            print(f"""
            ID: {plano[0]}
            Nome: {plano[1]}
            Preço: {plano[2]}
            Vantagens: {plano[3]}
            Desvantagens: {plano[4]}
            """)
    def limpando(self, nome_plano):
        comando = 'DELETE FROM plano WHERE nome_plano = %s'
        self.cursor.execute(comando, (nome_plano,))
        self.conexao.commit() #edita o banco de dados
    def alterando(self, nome, campo, valor_alterado):
        comando = f'UPDATE plano SET {campo} = %s WHERE nome_plano = %s'
        self.cursor.execute(comando, (valor_alterado, nome))
        self.conexao.commit()
    

conexao.close()