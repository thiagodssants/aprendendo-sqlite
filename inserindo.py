
import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

while True:
    print("1 - Inserir usuário")
    print("2 - Encerrar programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")

        comando_sql = "INSERT INTO usuarios (nome, email) VALUES (?, ?)"

        try:
            cursor.execute(comando_sql, (nome, email))
            conexao.commit()

            print(f"\nUsuário {nome} inserido com sucesso!")

        except sqlite3.IntegrityError:
            print("\nErro: email já cadastrado")

        except Exception as e:
            print(f"\nErro: {e}")

    elif opcao == "2":
        print("\nPrograma encerrado")
        break

    else:
        print("\nOpção inválida.")

conexao.close()
