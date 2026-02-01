## Controle de Estoque em Python

Este projeto foi desenvolvido com foco em aprendizado prático, simulando um sistema real de controle de estoque, muito comum em ambientes corporativos, especialmente para:

- Suporte técnico
- Sistemas administrativos
- Pequenos comércios
- Automação de processos

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
git clone https://github.com/seu-usuario/Controle-de-Estoque-Python.git
cd Controle-de-Estoque-Python
```
---
## Instalar dependências no Terminal
pip install flask

## Executar a aplicação no Terminal
python app.py

## Acessar o navegador no Terminal
http://127.0.0.1:5000
