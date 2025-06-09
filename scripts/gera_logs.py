import os
import datetime

def gerar_log(mensagem, arquivo="logs/log_status.txt"):
    """
    Gera logs com data e hora no arquivo especificado.
    Cria automaticamente a pasta 'logs/' se ela não existir.
    Usa codificação UTF-8 para suportar acentos e emojis.
    """
    # Cria a pasta 'logs' se não existir
    os.makedirs(os.path.dirname(arquivo), exist_ok=True)

    # Abre o arquivo no modo append (acrescentar), com codificação UTF-8
    with open(arquivo, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.datetime.now()}] {mensagem}\n")
