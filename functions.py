def numeros():
    print("1,2,3,4,5,6,7,8,9,11")

def Calculadora():
    num = int(input("Digite o Primeiro Numero:"))
    num2 = int(input("Digite o Segundo Numero:"))
    result = num + num2
    print(result)

def Multiplicador(num):
    result = num * num
    return result

def Retorno (num=2):
    result = num
    return result

print(Multiplicador(5))

print(Retorno())
print(Retorno(3))