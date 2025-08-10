import random

Contador ={} 
conta =[]


gasto = input("Digite o valor gasto: ")
categoria = input('Digite a categoria do gasto: ')

conta.append(categoria)
conta.append(gasto)

gerador_chave = '123456789!@#$%¨&*'
chave = ''

for i in range(10):
    chave += random.choice(gerador_chave)
    Contador = {chave: conta}

print(Contador)


    







