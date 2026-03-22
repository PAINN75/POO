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
ger_instrutor = GerenciadorInstrutor(conexao)
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
                        nome = input("Digite o nome do Instrutor que deseja adicionar!")
                        email = input("Digite o E-mail do instrutor!")
                        telefone = input("Digite o Telefone do instrutor!")
                        cpf = input("Digite o CPF do instrutor!")
                        especialidade = input("Digite a especialidade do instrutor")
                        ger_instrutor.adicionando(nome, cpf, email, telefone, especialidade)
                        print("Instrutor adicionado!")
                    case "2":
                        ger_instrutor.listando()
                    case "3":
                        name = input("Digite o nome do Instrutor que você deseja excluir!")
                        ger_instrutor.limpando(name)
                        print("Instrutor excluido!")
                    case "4":
                        campos_validos = {
                            "1": "nome_instrutor",
                            "2": "cpf_instrutor",
                            "3": "email_instrutor",
                            "4": "telefone_instrutor",
                            "5": "especialidade"
                        }
                        nome = input("Digite o nome do Instrutor que deseja alterar")
                        print("""
                        1 - Nome
                        2 - Email
                        3 - CPF      
                        4 - Telefone
                        5 - Especialidade
                        """)
                        opcao = input("Escolha o campo: ")
                        if opcao in campos_validos:
                            campo = campos_validos[opcao]
                            valor_alterado = input("Digite o novo valor: ")
                            print(f"Alterando {campo} do instrutor {nome}")
                            ger_instrutor.alterando(nome, campo, valor_alterado)
                        else:
                            print("Opção invalida")
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
                        nome = input("Digite o nome do Instrutor que deseja adicionar!")
                        preco = input("Digite o E-mail do instrutor!")
                        vantagens = input("Digite o Telefone do instrutor!")
                        desvantagens = input("Digite o CPF do instrutor!")    
                        ger_instrutor.adicionando(nome, preco, vantagens, desvantagens)
                        print("Plano adicionado!")
                    case "2":
                        ger_plano.listando()
                    case "3":
                        name = input("Digite o nome do Plano que você deseja excluir!")
                        ger_plano.limpando(name)
                        print("Plano excluido!")
                    case "4":
                        campos_validos = {
                            "1": "nome_plano",
                            "2": "preco_plano",
                            "3": "vantagens",
                            "4": "desvantagens",
                        }
                        nome = input("Digite o nome do Instrutor que deseja alterar")
                        print("""
                        1 - Nome
                        2 - Preço
                        3 - Vantagens     
                        4 - Desvantagens
                        """)
                        opcao = input("Escolha o campo: ")
                        if opcao in campos_validos:
                            campo = campos_validos[opcao]
                            valor_alterado = input("Digite o novo valor: ")
                            print(f"Alterando {campo} do plano {nome}")
                            ger_plano.alterando(nome, campo, valor_alterado)
                        else:
                            print("Opção invalida")
                    case "0":
                        break
                    case _:
                       print("Opção invalida!") 
        case "0":
            break
        case _:
            print("Opção invalida!")
conexao.close()