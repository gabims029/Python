import time 

#BIVLIOTECA PARA RETOMAR UM NÚMERO ALEATÓRIO 
from random import randint as rd #rd é o exemplo de nome dado
sorteado = rd(-100, 100) #sorteia um número de -100 a 100

#CRIANDO UMA LISTA DE NÚMEROS INTEIROS ALEATÓRIOS
lista = [rd(1, 6) for i in range(1, 11)]
lista2 = [x for x in range (1, 11)]
lista3 = ["Rolo compressor!!" for f in range (1, 4)]
# print(lista)
# print(lista2)
# print(lista3)

#CRIANDO LISTA PAR
par = [i for i in range(10) if i%2 == 0]
# print(par)

#!!!!POVOANDO UMA LISTA COM 'INPUT'!!!!#
# listaUsuario = [input ("Digite um número:") for s in range (5)]
# print(listaUsuario)

#UTILIZANDO O MÉTODO SPLIT (CADA PALAVRA SE TORNA UM ELEMENTO DA LISTA)
# nome = "Jonathan Calleri"
# print(nome)
# print(nome.split())

# APLICANDO O 'SPLIT' COM O INPUT
# notas = [n for n in input("Notas:").split()]
# print(notas)

# notas2 = [float(n) for n in input ("Notas:").split(",")]
# print(notas2)

#LISTA COM TIPOS DIFERENTES DE DADOS
# listaMista = [17, 70.5, "Com mundial!", True]
# print(listaMista)

# #MANIPULAÇÃO / FATIAMENTO DE LISTAS
# veiculos1 = ["carro", "bicicleta", "motor"]
# print("Veículos 1: ", veiculos1)

# #COPIANDO TODOO O CONTEÚDO DE UMA LISTA PARA OUTRA
# veiculos2 = veiculos1[:]
# del veiculos1[2]
# print("Veiculos 1:", veiculos1)
# print("Veiculos 2:", veiculos2)

# #COPIANDO PARTE DO CONTEÚDO DE UMA LISTA
# veiculos3 = veiculos2[0:1]
# print(veiculos3)

# #COPIANDO PARTE DE CONTEÚDO, INCLUINDO O ÚLTIMO ELEMENTO 
# veiculos4 = veiculos2[1:-1]
# print(veiculos4)

# # veiculos5 = veiculos2[-1: 1]
# # print(veiculos5)

# #OUTRAS MANEIRAS DE FATIAMENTO (OMISSÃO DO START OU DO END)
# myList = ["A", "B", "C", "D", "E", "F"]
# print(myList)
# newList = myList[:3] #começo 
# print(newList)
# newListFim = myList[5:] #fim
# print(newListFim)

# #APAGANDO CONTEÚDO DE LISTAS
# del myList[1:3]
# print(myList)
# del myList[:] #apaga todo o conteúdo
# print(myList)

#TESTANDO SE ALGUNS ITENS EXISTENTES EM UMA LISTA OU NÃO -- PARA ISSO, USAMOS PALAVRAS CHAVES IN E NOT IN:
naosei = ["A", "B", 18, 15]
print("A" in naosei)
print("C" not in naosei)
print(15 not in naosei)


time.sleep(2)