import mysql.connector
from modelos import Aluno, Plano, Instrutor
from crud  import GerenciadorAluno, GerenciadorPlano, GerenciadorInstrutor

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
                5- Contratar Personal    
                0- Sair            
                """)
                op = input()
                match op:
                    case "1":
                        nome = input("Digite o nome do aluno que deseja adicionar!").strip()
                        if not nome:
                            print("Erro: nome não pode ser vazio!")
                            continue
                        cpf = input("Digite o CPF do aluno!").strip()
                        if not cpf.isdigit() or len(cpf) != 11:
                            print("Erro: CPF inválido Digite 11 números sem pontos ou traços.")
                            continue
                        email = input("Digite o E-mail do aluno!").strip()
                        if "@" not in email or "." not in email:
                            print("Erro: E-mail invalido!")
                            continue
                        telefone = input("Digite o Telefone do aluno!").strip()
                        if not telefone.isdigit() or len(telefone) not in [10, 11]:
                            print("Erro: telefone invalido, Digite 10 ou 11 números.")
                            continue
                        print("Escolha um plano:")
                        ger_plano.listando()
                        id_plano = input("Digite o id do plano que você quer!").strip()
                        if not id_plano.isdigit():
                            print("Erro: ID inválido!")
                            continue
                        id_plano = int(id_plano)
                        aluno = Aluno(nome, cpf, email, telefone, id_plano)
                        ger_aluno.adicionando(aluno)
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
                    case "5":
                        nome_aluno = input("Digite o nome do aluno: ").strip()
                        if not nome_aluno:
                            print("Erro: nome não pode ser vazio!")
                            continue
                        print("Instrutores disponiveis: ")
                        ger_instrutor.listando()
                        id_instrutor = input("Digite o ID do Instrutor: ")
                        if not id_instrutor.isdigit():
                            print("Erro: ID inválido!")
                            continue
                        id_instrutor = int(id_instrutor)
                        ger_aluno. alterando(nome_aluno, "id_instrutor", id_instrutor)
                        print("Personal contratado!")
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
                        nome = input("Digite o nome do Instrutor que deseja adicionar!").strip()
                        if not nome:
                            print("Erro: nome não pode ser vazio!")
                            continue
                        cpf = input("Digite o CPF do Instrutor!").strip()
                        if not cpf.isdigit() or len(cpf) != 11:
                            print("Erro: CPF inválido Digite 11 números sem pontos ou traços.")
                            continue
                        email = input("Digite o E-mail do Instrutor!").strip()
                        if "@" not in email or "." not in email:
                            print("Erro: E-mail invalido!")
                            continue
                        telefone = input("Digite o Telefone do Instrutor!").strip()
                        if not telefone.isdigit() or len(telefone) not in [10, 11]:
                            print("Erro: telefone invalido, Digite 10 ou 11 números.")
                            continue
                        instrutor = Instrutor(nome, cpf, email, telefone)
                        ger_instrutor.adicionando(instrutor)
                        print("Instrutor adicionado!")
                    case "2":
                        ger_instrutor.listando()
                    case "3":
                        name = input("Digite o nome do Instrutor que você deseja excluir!").strip()
                        ger_instrutor.limpando(name)
                        print("Instrutor excluido!")
                    case "4":
                        campos_validos = {
                            "1": "nome_instrutor",
                            "2": "cpf_instrutor",
                            "3": "email_instrutor",
                            "4": "telefone_instrutor"
                        }
                        nome = input("Digite o nome do Instrutor que deseja alterar")
                        print("""
                        1 - Nome
                        2 - Email
                        3 - CPF      
                        4 - Telefone
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
                        nome = input("Digite o nome do Plano que deseja adicionar!").strip()
                        if not nome:
                            print("Erro: nome não pode ser vazio!")
                            continue
                        preco = input("Digite o preço: ").strip().replace(",", ".")
                        if not preco.replace(".", "").isdigit():
                            print("Erro: preço inválido!")
                            continue
                        preco = float(preco) 
                        vantagens = input("Digite a vantagens!").strip()
                        desvantagens = input("Digite a desvantagens!").strip()
                        plano = Plano(nome, preco, vantagens, desvantagens) 
                        ger_plano.adicionando(plano)
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