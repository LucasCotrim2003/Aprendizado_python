class Main:
    pass

print("Testando o projeto")

from Cliente import Cliente

from Conta import Conta

c1= Cliente("João", "114444-2222")

print(c1)
print(c1.nome," e ", c1.telefone)
conta=Conta(c1.nome,6565,0)
print(conta.titular," Numero: ",conta.numero, "Seu Saldo: ", conta.saldo)