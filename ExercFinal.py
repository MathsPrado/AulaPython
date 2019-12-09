print("Bem Vindo a sua Calculadora")

def valores():
    numero1 = int(input("Digite o primeiro Numero:"))
    numero2 = int(input("Digite o segundo Numero:"))
    return numero1, numero2


while True:
    numero1, numero2 = valores()
    print("""
    1. Soma
    2. Subtração
    3. Multiplicação
    4. Divisão
    5. Sair""")
    opcao = int(input("Digite a opçcão desejada: "))
    if opcao == 1:
        soma = numero1 + numero2
        print(f"O resultado da Soma é: {soma}")
    elif opcao == 2:
        sub = numero1 - numero2
        print(f"O resultado da subtração é: {sub}")
    elif opcao == 3:
        mul = numero1 * numero2
        print(f"O resultado da Multiplicação é: {mul}")
    elif opcao == 4:
        div = numero1 / numero2
        print(f"O resultado da Divisão é: {div}")
    elif opcao == 5:
        print("Finalizado")
        break
    else:
        print("Opção não valida!!")


