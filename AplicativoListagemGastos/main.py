from database import criar_conexao, executar_query, fechar_conexao

conexao = criar_conexao("Financeiro.db")
executar_query(conexao, """
               CREATE TABLE IF NOT EXISTS categorias (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               valor FLOAT NOT NULL
               );
               """)
fechar_conexao(conexao)

def adicionar_item(categorias):
    categoria = input("Digite a categoria: ").strip()
    valor = input("Digite o valor: ").strip()
    try:
        valor_float = float(valor)
    except ValueError:
        print("Valor inválido. Por favor, insira um número.")
        return
    
    if not categoria:
        print("Categoria não pode ser vazia.")
        return
    if categoria not in categorias:
        categorias[categoria] = []
    categorias[categoria].append(valor)
    print("Item adicionado!")

    conexao = criar_conexao("Financeiro.db")
    query = "INSERT INTO categorias (nome, valor) VALUES (?, ?)"
    params = (categoria, float(valor))
    executar_query(conexao, query, params)
    fechar_conexao(conexao)

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

categorias = {}
atualizar_lista(categorias)
total = {}

# Exibe os totais após o uso do aplicativo
def calcular_totais(categorias):
    totais = {}
    for categoria, itens in categorias.items():
        total = sum(float(item) for item in itens)
        totais[categoria] = total
    return totais
print("\nTotais por categoria:")
totais = calcular_totais(categorias)  # <-- Add this line
for categoria, total in totais.items():
    print(f"{categoria}: {total}")
# Inicialização
categorias = {}
atualizar_lista(categorias)