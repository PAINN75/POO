from abc import ABC, abstractmethod

class Pessoa(ABC):

    def __init__(self, nome, cpf, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

    @abstractmethod
    def exibir_dados(self):
        pass
class Aluno(Pessoa):
    def __init__(self, nome, cpf, email, telefone, plano):
        super().__init__(nome, cpf, email, telefone)
        self.plano = plano
    
    def exibir_dados(self):
        return f"""Nome do aluno:{self.nome}
        CPF:{self.cpf}
        E-mail:{self.email}
        Telefone:{self.telefone}
        Plano:{self.plano.nome}
        """

class Instrutor(Pessoa):
    def __init__(self, nome, cpf, email, telefone, especialidade):
        super().__init__(nome, cpf, email, telefone)
        self.especialidade = especialidade
    def exibir_dados(self):
        return f"""
        Nome do Instrutor:{self.nome}
        CPF:{self.cpf}
        E-mail:{self.email}
        Telefone:{self.telefone}
        Especialidade:{self.especialidade}
        """
    
class Plano:
    def __init__(self, nome, preco, vantagens, desvantagens):
        self.nome = nome
        self.preco = preco
        self.vantagens = vantagens
        self.desvantagens = desvantagens

