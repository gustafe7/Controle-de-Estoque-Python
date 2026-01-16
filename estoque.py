produtos = []

try:
    with open("estoque.txt", "r") as arquivo:
        for linha in arquivo:
            nome, quantidade = linha.strip().split(";")
            produtos.append({
                "nome": nome,
                "quantidade": int(quantidade)
            })
except FileNotFoundError:
    pass

def salvar_estoque():
    with open("estoque.txt", "w") as arquivo:
        for produto in produtos:
            arquivo.write(f"{produto["nome"]};{produto["quantidade"]}\n")
while True:
    print("\n== GERENCIADOR DE ESTOQUE ===")
    print("1 - cadastrar produto")
    print("2 - listar produtos")
    print("3 - entrada de estoque")
    print("4 - saída de estoque")
    print("5 - sair")

    opcao = input("escolha uma opcao: ")

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
     salvar_estoque()
     print("produto cadastrado com sucesso!")

    elif opcao == "2":
     if not produtos:
        
        print("nenhum produto cadastrado.")
     else:
        
        print("\n--- ESTOQUE FINAL ---")
        for produto in produtos:
             
            print(f"{produto["nome"]} - quantidade: {produto["quantidade"]}") 

    elif opcao == "3":
        nome = input("nome do produto para entrada: ").strip().lower()
        encontrado = False
     
        for produto in produtos:
            if produto["nome"].lower() == nome:

               quantidade = int(input("quantidade a adicionar: "))

               produto["quantidade"] += quantidade

               salvar_estoque()
               print("entrada registrada com sucesso!")
               
               encontrado = True
               break

        if not encontrado:
            print("produto não encontrado.")    

    elif opcao == "4":
        nome = input("nome do produto para saída:").strip().lower()
        encontrado = False

        for produto in produtos:
            if produto["nome"].lower() == nome:
                quantidade = int(input("quantidade a retirar:"))

                if quantidade > produto["quantidade"]:
                    print("quantidade insuficiente em estoque.")

                else:
                    produto["quantidade"] -= quantidade
                    salvar_estoque()
                    print("saída registrada com sucesso!")

                encontrado = True
                break

        if not encontrado:
            print("produto não encontrado")
    
    elif opcao == "5":
     print("saindo do sistema...")
     break
    
    else:
        print("opcao inválida")

    