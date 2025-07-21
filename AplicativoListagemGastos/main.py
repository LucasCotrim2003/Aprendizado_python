def adicionar_item(categorias):
    categoria = input("Digite a categoria: ")
    valor = input("Digite o valor: ")
    if categoria not in categorias:
        categorias[categoria] = []
    categorias[categoria].append(valor)
    print("Item adicionado!")

def listar_itens(categorias):
    for categoria, itens in categorias.items():
        print(f"\nCategoria: {categoria}")
        for item in itens:
            print(f"- {item}")

def calcular_totais(categorias):
    for categoria, itens in categorias.items():
        # Convert item values to float before summing
        total[categoria] = sum(float(item) for item in itens)
    return total
  

def atualizar_lista(categorias):
    while True:
        acao = input("\nO que você quer fazer? (adicionar (add)/listar (l)/sair(s)): ").lower()
        if acao == 'add':
            adicionar_item(categorias)
        elif acao == 'l':
            listar_itens(categorias)
        elif acao == 's':
            break
# Inicialização
categorias = {}
atualizar_lista(categorias)
total = {}

# Exibe os totais após o uso do aplicativo
totais = calcular_totais(categorias)
print("\nTotais por categoria:")
for categoria, total in totais.items():
    print(f"{categoria}: {total}")
# Inicialização
categorias = {}
atualizar_lista(categorias)