## Controle de Estoque em Python

Projeto desenvolvido em Python com foco em praticar lógica de programação, estruturas de dados e manipulação de arquivos.  
O sistema funciona via terminal e permite gerenciar produtos em estoque de forma simples e eficiente.

---

## Funcionalidades

- Cadastrar produtos com quantidade inicial
- Listar produtos cadastrados
- Registrar entrada de estoque
- Registrar saída de estoque
- Impedir retirada maior que a quantidade disponível
- Persistência de dados em arquivo
- Menu interativo no terminal

---

## Sistema de Auditoria

O projeto possui um módulo de auditoria responsável por registrar todas as ações
realizadas no sistema.

São registradas:
- Cadastro de produtos
- Entradas e saídas de estoque
- Tentativas inválidas
- Erros operacionais

Os registros são armazenados no arquivo `auditoria.log`, contendo data, tipo da
ação e descrição detalhada.

---

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Flask
- HTML
- CSS
- Manipulação de arquivos
- Estruturas de dados (listas e dicionários)
- Git e GitHub

---

## ▶️ Como executar

```bash
python estoque.py
