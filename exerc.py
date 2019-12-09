lista = ["Messi", "Hazard", "Neymar"]

print("""
     1. Adicionar novos Jogadores
     2. Jogadores adicionados
     3. Buscar Jogador
     4. Sair
     """)

while True:

    opcao = int(input("Digite a opção desejada: "))


    if opcao == 1:
        pessoa = str(input("Digite o nome do jogador:"))
        lista.append(pessoa)

    elif opcao == 2:
        print(lista)

    elif opcao == 3:
        jogador = input("Digite o Nome do Jogador:")
        if jogador in lista:
            print(f"O Jogador {jogador} Já está cadastrado. ")
        else: print(f"O Jogador {jogador} não está cadastrado")

    elif opcao == 4:
        print("Saindo...")
        break

    else:
        print("Opção Invalida")

