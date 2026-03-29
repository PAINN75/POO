from modelos import Aluno, Plano, Instrutor
from abc import ABC, abstractmethod

class Gerenciador(ABC):
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = conexao.cursor()
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
        super().__init__(conexao)
    def adicionando(self, aluno):
        comando = 'INSERT INTO aluno (nome_aluno, cpf_aluno, email_aluno, telefone_aluno, id_plano, id_instrutor) VALUES (%s, %s, %s, %s, %s, %s)'
        valores = (aluno.nome, aluno.cpf, aluno.email, aluno.telefone, aluno.id_plano, aluno.id_instrutor)
        self.cursor.execute(comando, valores)
        self.conexao.commit()
    def listando(self):
        comando = 'SELECT * FROM aluno'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() # ler o banco de dados
        if not resultado:
            print("Nenhum aluno cadastrado")
            return
        for aluno in resultado:
            obj = Aluno(aluno[1],  aluno[2], aluno[3], aluno[4], aluno[5])
            print(obj)
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
        super().__init__(conexao)
    def adicionando(self, instrutor):
        comando = 'INSERT INTO instrutor (nome_instrutor, cpf_instrutor ,email_instrutor, telefone_instrutor) VALUES (%s, %s, %s, %s)'
        valores = (instrutor.nome, instrutor.cpf, instrutor.email, instrutor.telefone)
        self.cursor.execute(comando, valores)
        self.conexao.commit()
    def listando(self):
        comando = 'SELECT * FROM instrutor'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() # ler o banco de dados
        if not resultado:
            print("Nenhum Instrutor encontrado!")
            return
        for instrutor in resultado:
            obj = Instrutor(instrutor[1], instrutor[2], instrutor[3], instrutor[4])
            print(obj)
    
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
        super().__init__(conexao)
    def adicionando(self, plano):
        comando = 'INSERT INTO plano (nome_plano,  preco_plano, vantagens, desvantagens) VALUES (%s, %s, %s, %s)'
        valores = (plano.nome, plano.preco, plano.vantagens, plano.desvantagens)
        self.cursor.execute(comando, valores)
        self.conexao.commit()
    def listando(self):
        comando = 'SELECT * FROM plano'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() # ler o banco de dados
        if not resultado:
            print("Nenhum Plano encontrado!")
            return
        for plano in resultado:
            obj = Plano(plano[1], plano[2], plano[3], plano[4])
            print(obj)
    def limpando(self, nome_plano):
        comando = 'DELETE FROM plano WHERE nome_plano = %s'
        self.cursor.execute(comando, (nome_plano,))
        self.conexao.commit() #edita o banco de dados
    def alterando(self, nome, campo, valor_alterado):
        comando = f'UPDATE plano SET {campo} = %s WHERE nome_plano = %s'
        self.cursor.execute(comando, (valor_alterado, nome))
        self.conexao.commit()