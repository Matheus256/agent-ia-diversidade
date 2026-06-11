import logging
import os
from datetime import datetime

def nome_mes(mes):
    meses = {
        "01": "JANEIRO", "02": "FEVEREIRO", "03": "MARÇO", "04": "ABRIL",
        "05": "MAIO", "06": "JUNHO", "07": "JULHO", "08": "AGOSTO",
        "09": "SETEMBRO", "10": "OUTUBRO", "11": "NOVEMBRO", "12": "DEZEMBRO"
    }
    return meses[mes]

def configurar_logger(nome_base="inspetor"):
    logger = logging.getLogger(nome_base)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger
    
    time = datetime.now()
    ano = time.strftime("%Y")
    mes = time.strftime("%m")
    data = time.strftime("%d-%m-%y")
    nomemes = nome_mes(mes)

    pasta_logs = os.path.join("logs", ano, f"{nomemes}")
    os.makedirs(pasta_logs, exist_ok=True)

    # 1. Alterado de .log para .md
    caminho_arquivo = os.path.join(pasta_logs, f"{nome_base}_{data}.md")

    # Se o arquivo for novo, cria o cabeçalho da tabela Markdown
    novo_arquivo = not os.path.exists(caminho_arquivo)

    # 2. Formato configurado como linha de tabela Markdown
    formato = "%(asctime)s - **[%(levelname)s]** -- %(message)s"
    formato_data = "%H:%M:%S"

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(formato, formato_data))

    file_handler = logging.FileHandler(caminho_arquivo, encoding="utf-8")
    file_handler.setFormatter(logging.Formatter(formato, formato_data))

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # 3. Escreve o cabeçalho da tabela se o arquivo acabou de ser criado
    if novo_arquivo:
        with open(caminho_arquivo, "a", encoding="utf-8") as f:
            f.write(f"# Logs de {data}\n\n")

    return logger
