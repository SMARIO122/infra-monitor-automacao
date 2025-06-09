import subprocess
import datetime
from gera_logs import gerar_log

# Lista de serviços a serem monitorados
servicos = ["nginx", "docker", "cron"]

def verificar_servico(servico):
    """
    Verifica se o serviço está ativo no sistema usando systemctl (Linux).
    Retorna True se ativo, False se inativo ou inexistente.
    """
    try:
        resultado = subprocess.run(
            ["systemctl", "is-active", servico],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        # strip() limpa espaços e quebras de linha
        return resultado.stdout.strip() == "active"
    except Exception as e:
        gerar_log(f"Erro ao verificar {servico}: {e}")
        return False

def monitorar_servicos():
    """
    Percorre a lista de serviços e registra o status no log.
    """
    gerar_log("🔍 Iniciando verificação de serviços...")

    for servico in servicos:
        status = verificar_servico(servico)
        if status:
            gerar_log(f"✅ {servico} está ativo.")
        else:
            gerar_log(f"❌ {servico} está inativo ou não encontrado.")

    gerar_log("✅ Monitoramento finalizado.\n")

# Execução direta (quando não for importado como módulo)
if __name__ == "__main__":
    monitorar_servicos()
