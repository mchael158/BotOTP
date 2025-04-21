import pyautogui
import csv
import time
from datetime import datetime

ARQUIVO_ENTRADA = "teclas_registradas.csv"

def ler_teclas_csv():
    with open(ARQUIVO_ENTRADA, newline='') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  # Pula o cabeçalho
        return [(linha[0], linha[1]) for linha in leitor]

def calcular_intervalos(dados):
    tempos = [datetime.strptime(h, "%H:%M:%S") for h, _ in dados]
    intervalos = [0]  # Primeiro não tem espera
    for i in range(1, len(tempos)):
        delta = (tempos[i] - tempos[i - 1]).total_seconds()
        intervalos.append(max(delta, 0))  # Evita tempo negativo
    return intervalos

def reproduzir_movimentos(dados, intervalos):
    print("Reproduzindo movimentos...")
    for (horario, tecla), espera in zip(dados, intervalos):
        time.sleep(espera)
        print(f"{horario} -> Pressionando {tecla}")
        pyautogui.press(tecla.lower())

    print("Reprodução finalizada.")

dados = ler_teclas_csv()
intervalos = calcular_intervalos(dados)
reproduzir_movimentos(dados, intervalos)
