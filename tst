print("Bem vindo")

numero1 = int(input("Digite o primeiro Numero:"))
numero2 = int(input("Digite o segundo Numero"))

while True:
    print("""
    1. Soma
    2. Subtração
    3. Multiplicação
    4. Divisão
    5. Sair""")
    opcao = int(input("Digite a opçcão desejada: "))
    if opcao == 1:
        soma = numero1 + numero2
        print(soma)
    elif opcao == 2:
        sub = numero1 - numero2
        print(sub)
    elif opcao == 3:
        mul = numero1 * numero2
        print(mul)
    elif opcao == 4:
        div = numero1 / numero2
        print(div)
    elif opcao == 5:
        print("Finalizado")
        break
    else:
        print("Opção não valida!!")


