print(7 ** 4)

string = "Olá, pai!"
print(string)
print(string.split())

planeta = "Terra"
distancia = "123456789km"

print("Distancia: O planeta {a} está a um total de {b}".format(a=planeta, b=distancia))

lst = [1,1,[3,4],[5,[100,200,['olá']],23,11],1,7]

print(lst[3][1][2])

d = {'k1':[1,2,3,{'café':['Banana','mulher','colher',{'alvo':[1,2,3,"olá"]}]}]}

print(d)
print("---------------------------++--------------------------------")
print(d['k1'][3]['café'][3]['alvo'][3])


print("---------------------------++--------------------------------")


def dominio(email):
    saida = email.split('@')[-1]    #[-1] pega a ultima
    print(saida)
    return saida

dominio("matheus.lima@summit-bra.com")

txt = "welcome to the jungle"
x = txt.split()[0]
print(x)


def encontraCachorro(string):
    return 'cachorro' in string.lower()

print(encontraCachorro("existe um cachorro aqui?"))

def contaCachorro(string):
    count = 0
    for palavra in string.lower().split():
        if palavra == "cachorro":
            count = count + 1
    return count

print(contaCachorro("cachorro é um cachorro muito cachorro"))
