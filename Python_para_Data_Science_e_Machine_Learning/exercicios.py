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
