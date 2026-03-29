from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

    @abstractmethod
    def __str__(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, cpf, email, telefone, id_plano):
        super().__init__(nome, cpf, email, telefone)
        self.id_plano = id_plano
    def __str__(self):
        return (f"\n        Nome:     {self.nome}"
                f"\n        CPF:      {self.cpf}"
                f"\n        E-mail:   {self.email}"
                f"\n        Telefone: {self.telefone}"
                f"\n        Plano ID: {self.id_plano}"
                f"\n        {'-' * 30}")
class Instrutor(Pessoa):
    def __init__(self, nome, cpf, email, telefone):
        super().__init__(nome, cpf, email, telefone)
    def __str__(self):
        return (f"\n        Nome:          {self.nome}"
                f"\n        CPF:           {self.cpf}"
                f"\n        E-mail:        {self.email}"
                f"\n        Telefone:      {self.telefone}"
                f"\n        {'-' * 30}")
class Plano:
    def __init__(self, nome, preco, vantagens, desvantagens):
        self.nome = nome
        self.preco = preco
        self.vantagens = vantagens
        self.desvantagens = desvantagens

    def __str__(self):
        return (f"\n        Nome:         {self.nome}"
                f"\n        Preço:        R$ {self.preco}"
                f"\n        Vantagens:    {self.vantagens}"
                f"\n        Desvantagens: {self.desvantagens}"
                f"\n        {'-' * 30}")

