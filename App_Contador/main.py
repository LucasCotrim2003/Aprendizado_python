import random

Contador ={} 
conta =[]
gasto = 0
categoria = 'a'

while True:
    
    gasto = input("Digite o valor gasto (ou cancelar para sair): ")
    if gasto == 'cancelar':
         print("Saindo do programa...")
         break
    else:
        print("Gasto inserido!")


    categoria = input('Digite a categoria do gasto (ou cancelar para sair): ')
    if categoria == 'cancelar':
        print("Saindo do programa...")
        break
    else:
        print("Categoria adicionada!")

    conta.append(categoria)
    conta.append(gasto)

    gerador_chave = '123456789!@#$%¨&*'
    chave = ''

    for i in range(10):
        chave += random.choice(gerador_chave)
        Contador = {chave: conta}

    print(Contador)




    







