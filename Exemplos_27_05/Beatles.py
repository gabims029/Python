import time

beatles = []
print("Etapa 1:", beatles)

#acrescenta os nomes dos cantores na lista
beatles.append("John Lennon, Paul McCartney e George Harrison")
print("Etapa 2:", beatles)

#solicita que o usuario digite o nome 
for i in range(2):
    beatles.append(input("Digite o nome do cantor Stu Stucliffe ou Pete Best:"))
print("Etapa 3:", beatles)

#deleta oos nomes
del beatles[-1] 
del beatles[-1]
print("Etapa 4:", beatles)

#acrescenta o nome no primeiro lugar da lista 
beatles.insert(0, "Ringo Starr")
print("Etapa 5:", beatles)

time.sleep(2)