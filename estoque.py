# Importa a função responsável por registrar ações no arquivo de log
# (cadastro, entrada, saída e erros)
from auditoria import registrar_acao

# Nome do arquivo que armazena os dados do estoque
ARQUIVO_ESTOQUE = "estoque.txt"

# Lista em memória que representa o estoque atual
# Cada item será um dicionário: {"nome": str, "quantidade": int}
produtos = []

# FUNÇÃO: carregar_estoque
# ---------------------------------------------------------
# Lê o arquivo estoque.txt e carrega os produtos na lista
# 'produtos'. Essa função sempre limpa a lista antes
# de carregar para evitar duplicações.

def carregar_estoque():
    produtos.clear()  # Limpa a lista antes de recarregar os dados

    try:
        # Abre o arquivo de estoque em modo leitura
        with open(ARQUIVO_ESTOQUE, "r") as arquivo:
            for linha in arquivo:
                # Cada linha do arquivo tem o formato: nome;quantidade
                nome, quantidade = linha.strip().split(";")

                # Adiciona o produto na lista em memória
                produtos.append({
                    "nome": nome,
                    "quantidade": int(quantidade)
                })
    except FileNotFoundError:
        # Caso o arquivo ainda não exista,
        # o estoque inicia vazio
        pass

# FUNÇÃO: salvar_estoque
# ---------------------------------------------------------
# Grava o conteúdo da lista 'produtos' no arquivo estoque.txt.
# Essa função é chamada sempre que o estoque sofre alterações.

def salvar_estoque():
    # Abre o arquivo em modo escrita (sobrescreve o conteúdo)
    with open(ARQUIVO_ESTOQUE, "w") as arquivo:
        for produto in produtos:
            # Salva cada produto no formato: nome;quantidade
            arquivo.write(
                f"{produto['nome']};{produto['quantidade']}\n"
            )

# FUNÇÃO: listar_produtos
# ---------------------------------------------------------
# Retorna todos os produtos cadastrados no estoque.
# Sempre recarrega os dados do arquivo antes de retornar.

def listar_produtos():
    carregar_estoque()
    return produtos

# FUNÇÃO: cadastrar_produto
# ---------------------------------------------------------
# Cadastra um novo produto no estoque com quantidade inicial.
# Também registra a ação no arquivo de auditoria (.log).

def cadastrar_produto(nome, quantidade):
    carregar_estoque()

    # Verifica se já existe produto com o mesmo nome
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            return False  # Produto já existe

    # Se não existir, cadastra
    produtos.append({
        "nome": nome,
        "quantidade": quantidade
    })

    salvar_estoque()

    registrar_acao(
        "CADASTRO",
        f"Produto '{nome}' cadastrado com quantidade inicial {quantidade}"
    )

    return True  # Cadastro realizado com sucesso


    # Salva o estoque atualizado no arquivo
    salvar_estoque()

    # Registra a ação de cadastro no log
    registrar_acao(
        "CADASTRO",
        f"Produto '{nome}' cadastrado com quantidade inicial {quantidade}"
    )

# FUNÇÃO: entrada_estoque
# ---------------------------------------------------------
# Aumenta a quantidade de um produto existente.
# Retorna True se o produto for encontrado,
# ou False caso não exista.

def entrada_estoque(nome, quantidade):
    carregar_estoque()

    for produto in produtos:
        # Compara os nomes ignorando maiúsculas/minúsculas
        if produto["nome"].lower() == nome.lower():
            produto["quantidade"] += quantidade
            salvar_estoque()

            # Registra a entrada no log
            registrar_acao(
                "ENTRADA",
                f"Entrada de {quantidade} unidades no produto '{nome}'"
            )
            return True

    # Produto não encontrado
    return False

# FUNÇÃO: saida_estoque
# ---------------------------------------------------------
# Reduz a quantidade de um produto existente.
# Impede que o estoque fique negativo.
# Retorna True em caso de sucesso ou False em caso de erro.

def saida_estoque(nome, quantidade):
    carregar_estoque()

    for produto in produtos:
        if produto["nome"].lower() == nome.lower():

            # Validação para evitar estoque negativo
            if quantidade > produto["quantidade"]:
                registrar_acao(
                    "ERRO",
                    f"Tentativa de saída maior que o estoque do produto '{nome}'"
                )
                return False

            # Atualiza a quantidade do produto
            produto["quantidade"] -= quantidade
            salvar_estoque()

            # Registra a saída no log
            registrar_acao(
                "SAIDA",
                f"Saída de {quantidade} unidades do produto '{nome}'"
            )
            return True

    # Produto não encontrado
    return False


    