from flask import Flask, render_template, request
from estoque import (
    listar_produtos,
    cadastrar_produto,
    entrada_estoque,
    saida_estoque,
    excluir_produto_estoque
)

app = Flask(__name__)

# Página inicial
@app.route("/")
def index():
    produtos = listar_produtos()
    return render_template(
        "index.html",
        produtos=produtos,
        mensagem_cadastro=None,
        mensagem_entrada=None,
        mensagem_saida=None,
        mensagem_exclusao=None
    )

# Cadastro de produto
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    quantidade = int(request.form["quantidade"])

    sucesso = cadastrar_produto(nome, quantidade)

    if sucesso:
        mensagem_cadastro = "Produto cadastrado com sucesso"
    else:
        mensagem_cadastro = "Um produto com esse nome já foi cadastrado"

    produtos = listar_produtos()

    return render_template(
        "index.html",
        produtos=produtos,
        mensagem_cadastro=mensagem_cadastro,
        mensagem_entrada=None,
        mensagem_saida=None,
        mensagem_exclusao=None
    )

# Entrada de estoque
@app.route("/entrada", methods=["POST"])
def entrada():
    nome = request.form["nome"]
    quantidade = int(request.form["quantidade"])

    sucesso = entrada_estoque(nome, quantidade)

    if sucesso:
        mensagem_entrada = "Entrada registrada com sucesso"
    else:
        mensagem_entrada = "Produto não encontrado"

    produtos = listar_produtos()

    return render_template(
        "index.html",
        produtos=produtos,
        mensagem_cadastro=None,
        mensagem_entrada=mensagem_entrada,
        mensagem_saida=None,
        mensagem_exclusao=None
    )

# Saída de estoque
@app.route("/saida", methods=["POST"])
def saida():
    nome = request.form["nome"]
    quantidade = int(request.form["quantidade"])

    sucesso = saida_estoque(nome, quantidade)

    if sucesso:
        mensagem_saida = "Saída registrada com sucesso"
    else:
        mensagem_saida = "Erro na saída de estoque"

    produtos = listar_produtos()

    return render_template(
        "index.html",
        produtos=produtos,
        mensagem_cadastro=None,
        mensagem_entrada=None,
        mensagem_exclusao=None,
        mensagem_saida=mensagem_saida
    )

@app.route("/excluir", methods=["POST"])
def excluir():
    nome = request.form["nome"]

    sucesso = excluir_produto_estoque(nome)

    if sucesso:
        mensagem = "Produto excluído com sucesso"

    else:
        mensagem = "Produto não encontrado"

    produtos = listar_produtos()

    return render_template(
        "index.html",
        produtos=produtos,
        mensagem_cadastro=None,
        mensagem_entrada=None,
        mensagem_saida=None,
        mensagem_exclusao=mensagem
)

if __name__ == "__main__":
    app.run(debug=True)

