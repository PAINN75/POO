import mysql.connector
from modelos import Aluno, Plano, Instrutor
from crud  import GerenciadorAluno, GerenciadorPlano, GerenciadorInstrutor
from abc import ABC, abstractmethod
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mned2003@',
    database='bdacademia',
)
ger_aluno = GerenciadorAluno(conexao)
ger_plano = GerenciadorPlano(conexao)
ger_intrutor = GerenciadorInstrutor(conexao)
while True:
    print("-" * 30)
    print("Menu principal")
    print("-" * 30)
    print("Escolha uma opção em que voçê quer gerenciar")
    print("""
    1- Alunos
    2- Instrutores
    3- Planos
    0- Sair            
    """)
    print("-" * 30)
    opcao = input()
    match opcao:
        case "1":
            while True:
                print("-" * 30)
                print("Escolha uma opção!")
                print("""
                1- Adicionar
                2- Listar
                3- Remover
                4- Altualizar      
                0- Sair            
                """)
                op = input()
                match op:
                    case "1":
                        nome = input("Digite o nome do aluno que deseja adicionar!")
                        email = input("Digite o E-mail do aluno!")
                        telefone = input("Digite o Telefone do aluno!")
                        cpf = input("Digite o CPF do aluno!")
                        print("Escolha um plano:")
                        ger_plano.listando()
                        id_plano = int(input("Digite o id do plano que você quer!"))
                        ger_aluno.adicionando(nome, email, telefone, cpf, id_plano)
                        print("Aluno adicionado!")
                    case "2":
                        ger_aluno.listando()
                    case "3":
                        name = input("Digite o nome do aluno que você deseja excluir!")
                        ger_aluno.limpando(name)
                        print("Aluno excluido!")
                    case "4":
                        campos_validos = {
                            "1": "nome_aluno",
                            "2": "email_aluno",
                            "3": "telefone_aluno",
                            "4": "cpf_aluno"
                        }
                        nome = input("Digite o nome do aluno que deseja alterar")
                        print("""
                        1 - Nome
                        2 - Email
                        3 - Telefone
                        4 - CPF
                        """)
                        opcao = input("Escolha o campo: ")
                        if opcao in campos_validos:
                            campo = campos_validos[opcao]
                            valor_alterado = input("Digite o novo valor: ")
                            print(f"Alterando {campo} do aluno {nome}")
                            ger_aluno.alterando(nome, campo, valor_alterado)
                        else:
                            print("Opção invalida")
                    case "0":
                        break
                    case _:
                       print("Opção invalida!") 
        case "2":
            while True:
                print("-" * 30)
                print("Escolha uma opção!")
                print("""
                1- Adicionar
                2- Listar
                3- Remover
                4- Altualizar      
                0- Sair            
                """)
                op = input()
                match op:
                    case "1":
                        pass
                    case "2":
                        ger_intrutor.listando()
                    case "3":
                        name = input("Digite o nome do Instrutor que você deseja excluir!")
                        ger_intrutor.limpando(name)
                        print("Instrutor excluido!")
                    case "4":
                        pass
                    case "0":
                        break
                    case _:
                       print("Opção invalida!") 
        case "3":
            while True:
                print("-" * 30)
                print("Escolha uma opção!")
                print("""
                1- Adicionar
                2- Listar
                3- Remover
                4- Altualizar      
                0- Sair            
                """)
                op = input()
                match op:
                    case "1":
                        pass
                    case "2":
                        ger_plano.listando()
                    case "3":
                        name = input("Digite o nome do Plano que você deseja excluir!")
                        ger_plano.limpando(name)
                        print("Plano excluido!")
                    case "4":
                        pass
                    case "0":
                        break
                    case _:
                       print("Opção invalida!") 
        case "0":
            break
        case _:
            print("Opção invalida!")
conexao.close()