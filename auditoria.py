from datetime import datetime

def registrar_acao(acao, descricao):
    data_hora = datetime.now().strftime("%d/%m/%y %H:%M:%S")


    with open("auditoria.log", "a", encoding="utf_8") as arquivo:
         arquivo.write(f"[{data_hora}] {acao} - {descricao}\n")
    