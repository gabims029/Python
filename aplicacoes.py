import time

#ENCONTRAR O MAIOR VALOR NA LISTA - EXEMPLO 1
lista = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maiorNumero = lista[0] #recebeu o número 17 

for i in range(1, len(lista)):
    if lista[i] > maiorNumero:
        maior_numero = lista[i]
print("O maior número da lista é:", maiorNumero)

#EXEMPLO 2
myList = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior = myList[0]
for i in myList:
    if i > maior:
        maior = i
print("Maior valor 2: ", maior)

#EXEMPLO 3
ultimaLista = myList[:]
mel = ultimaLista[0]
for i in ultimaLista[1:]:
    if i > mel:
        mel = 1
print("Maior valor 3: ", mel)       

#ENCONTRAR A LOCALizacao de um determinado elemneto dentro de uma lista
frutas = ["abacaxi", "maçã", "pêra", "mamão", "uva", "melancia"]
elemento = "melancia"
achado = False

for i in range(len(frutas)):
    achado = frutas[i == elemento]
    if achado:
        break

if achado:
    print("Elemento encontrado no indice", i)
else:
    print("Não encontrado!")

#CONFERIDOR DE APOSTA EM LOTERIA
sorteados = [5, 11, 9, 42, 3, 49]
apostados = [3, 7, 11, 42, 34, 49]
acertos = 0

for numero in sorteados:
    if numero in apostados:
        acertos += 1
print(acertos)

#REMOÇÃO DE NÚMEROS REPETIDOS EM UMA LISTA
lista = [1, 2, 4, 4, 1, 4, 2, 6, 9]
print("Lista original:", lista)

#LISTA DE APOIO 
visto = []

#INTERAR PELA LISTA ORIGINAL DE TRÁS PARA FRENTE
for i in range(len(lista) -1, -1, -1):
    #se o número já está na lista "vistos", removê-lo da lista original
    if lista[i] in visto:
        del lista[1]
    else:
        #caso contrário, adicionar á lista "vistos"
        visto.append(lista[i])
#exibir a lista original modificada
print("Lista modificada:", lista)






time.sleep(2)