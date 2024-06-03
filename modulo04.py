import time

#FUNÇÃO QUE POSSUE MUITAS ATRIBUIÇÕES, MAS PARECE
# def somar():
#     n1 = int(input("Digite o primeiro número da adção: "))
#     n2 = int(input("Digite o segundo número da adção: "))
#     print(n1 + n2)
# somar()

#FUNÇÃO EXCLUSIVA DE SOMA DE DOIS NÚMEROS 
def somar2(n1, n2):
    soma = n1 + n2
    return soma

# print("Soma 2: ",somar2(22, 20))

#TERCEIRO EXEMPLO DE FUNÇÃO
def somar3(n1, n2):
    return n1 +n2
# numero1 = float(input("Digite um número:"))
# numero2 = float(input("Digite outro número:"))

#CHAMADA DA FUNÇÃO
# print(somar3(numero1, numero2))

#CHAMADA DA FUNÇÃO
print(somar3(n2 = 12, n1 = 5))

#FUNÇÃO COM PARÂMETROS DEFAULT (PADÃO)
def somar4(n1 = 0, n2 = 0):
    return n1 + n2

# print(somar4(50, 25))
# print(somar4)

#Função com apenas alguns valores defalt
def somar5 (n1, n2 = 0):
    return n1 + n2
print(somar4(50, 25)) #75
#print(somar4) #erro
print(somar5(10)) #10
print(somar5(n2 = 51, n1 = 12))

def somar6(n1, n2):
    if n1 == 1:
        return 1
print(somar6(1, 3)) #True
print(somar6(13,3)) #None

print(somar6(1, 2) + 10) #mostra 11
print(somar6(2, 2) + 10) #mostra tipo não suportado

time.sleep(2)