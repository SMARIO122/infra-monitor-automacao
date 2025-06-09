import os #importando bibliotecas
import datetime

servicos = ["nginx", "docker", "cron"]
log_file = "log_status.txt"

def verificar(servico):
    status = os.system(f"systemctl is-active --quiet {servico}")
    return "ativo" if status == 0 else "inativo"

with open(log_file, "a") as log:
    log.write(f"\n📅 Verificação em {datetime.datetime.now()}\n")
    for servico in servicos:
        estado = verificar(servico)
        log.write(f"🔍 {servico}: {estado}\n")
    log.write("—" * 30 + "\n")
