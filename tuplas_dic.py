import time

tupla = tuple()

tupla = (1)

tupla = (1,)

tupla = 1, 2, 3

print(tupla)

print(tupla[1])

#tupla[0] = 100 #ERRO POIS NÃO É POSSÍVEL ALTERAR UMA TUPLA 

#MANIPULANDO DICIONÁRIOS: 
dic = {"semMundial":"Palmeiras", "1mundial":"Corinthians", "2mundiais":"SãoPaulo"}

print(dic["semMundial"])

notas ={"mat":5, "lp":10, "ef":8}

print(notas)
print(notas["lp"])

#print(notas["bio"])

print(dir(notas))

print(notas.values())

print(notas.keys())

print(len(notas))

for disciplina in notas.keys():
    print(disciplina)

print("ola!")

time.sleep(2)