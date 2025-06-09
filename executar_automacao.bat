@echo off
cd %~dp0scripts
python verifica_servicos.py
python gera_logs.py
