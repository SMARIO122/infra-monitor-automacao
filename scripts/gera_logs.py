import datetime

def gerar_log(mensagem, arquivo="logs/log_status.txt"):
    with open(arquivo, "a") as log:
        log.write(f"[{datetime.datetime.now()}] {mensagem}\n")

# Exemplo de uso
if __name__ == "__main__":
    gerar_log("Sistema de log inicializado com sucesso.")
