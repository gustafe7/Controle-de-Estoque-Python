# GERENCIADOR DE ESTOQUE EM PYTHON
# Programa para cadastrar produtos, controlar entrada e saída
# e salvar os dados em arquivo de forma persistente.

from auditoria import registrar_acao # Importa a função responsável por registrar ações no sistema de auditoria
produtos = []  # lista que vai armazenar os produtos cadastrados

# Carregar dados do arquivo estoque.txt, caso exista
# Cada linha do arquivo deve ter o formato: nome;quantidade

try:
    with open("estoque.txt", "r") as arquivo:
        for linha in arquivo:
            nome, quantidade = linha.strip().split(";")
            produtos.append({
                "nome": nome,
                "quantidade": int(quantidade)
            })
except FileNotFoundError:
    # Caso o arquivo não exista, a lista de produtos começa vazia
    pass

# Função para salvar o estoque atual no arquivo

def salvar_estoque():
    with open("estoque.txt", "w") as arquivo:
        for produto in produtos:
            arquivo.write(f"{produto['nome']};{produto['quantidade']}\n")

# Loop principal do sistema

while True:
    print("\n=== GERENCIADOR DE ESTOQUE ===")
    print("1 - cadastrar produto")
    print("2 - listar produtos")
    print("3 - entrada de estoque")
    print("4 - saída de estoque")
    print("5 - sair")

    opcao = input("escolha uma opcao: ")

    # Cadastro de novo produto
    
    if opcao == "1":
        nome = input("nome do produto: ").strip()
        if nome == "":
            print("nome inválido.")
            continue
        quantidade = int(input("quantidade inicial: "))
        produto = {
            "nome": nome,
            "quantidade": quantidade
        }
        produtos.append(produto)
        salvar_estoque()  # salva o estoque após cadastro

        # Registra a ação de cadastro no sistema de auditoria
        
        registrar_acao(
            "CADASTRO",
            f"Produto '{nome}' cadastrado com quantidade inicial: {quantidade}"
        )

        print("produto cadastrado com sucesso!")

    # Listar todos os produtos cadastrados
    
    elif opcao == "2":
        if not produtos:
            print("nenhum produto cadastrado.")
        else:
            print("\n--- ESTOQUE FINAL ---")
            for produto in produtos:
                print(f"{produto['nome']} - quantidade: {produto['quantidade']}") 

    # Entrada de estoque (aumentar quantidade)
    
    elif opcao == "3":
        nome = input("nome do produto para entrada: ").strip().lower()
        encontrado = False
        for produto in produtos:
            if produto["nome"].lower() == nome:
                quantidade = int(input("quantidade a adicionar: "))
                produto["quantidade"] += quantidade
                salvar_estoque()  # salva após a entrada

                # Registra a entrada no log de auditoria
                
                registrar_acao(
                    "CADASTRO",
                    f"Produto '{nome}' cadastrado com quantidade inicial: {quantidade}"
                )

                print("entrada registrada com sucesso!")
                encontrado = True
                break

        if not encontrado:
            print("produto não encontrado.")    

    # Saída de estoque (reduzir quantidade)
    
    elif opcao == "4":
        nome = input("nome do produto para saída:").strip().lower()
        encontrado = False
        for produto in produtos:
            if produto["nome"].lower() == nome:
                quantidade = int(input("quantidade a retirar: "))
                
                # Validação para impedir estoque negativo
                
                if quantidade > produto["quantidade"]:
                    print("quantidade insuficiente em estoque.")

                    # Registra tentativa inválida no log
                    
                    registrar_acao(
                        "ERRO",
                        f"Tentativa de retirada maior que o estoque do produto '{produto['nome']}'"
                    )
                else:
                    produto["quantidade"] -= quantidade
                    salvar_estoque()  # salva após a saída

                    registrar_acao(
                        "SAIDA",
                        f"Saída de {quantidade} unidades do produto '{produto['nome']}'" 
                    )

                    print("saída registrada com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("produto não encontrado")

    # Sair do sistema

    elif opcao == "5":
        print("saindo do sistema...")
        break

    # Opção inválida digitada
    
    else:
        print("opcao inválida")

    