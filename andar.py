import csv
import time
import pyautogui

def ler_coordenadas_do_arquivo(arquivo_csv):
    coordenadas = []
    with open(arquivo_csv, newline='') as f:
        reader = csv.reader(f)
        for linha in reader:
            if len(linha) < 2:
                continue
            partes = linha[1].replace(" ", "").split(",")
            if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
                coordenadas.append((int(partes[0]), int(partes[1])))
    return coordenadas

def mover_para_direcao(atual, proxima):
    x1, y1 = atual
    x2, y2 = proxima

    if x2 > x1:
        pyautogui.press('right')
    elif x2 < x1:
        pyautogui.press('left')
    elif y2 > y1:
        pyautogui.press('down')
    elif y2 < y1:
        pyautogui.press('up')

print("Executando movimento baseado em coordenadas...")
coordenadas = ler_coordenadas_do_arquivo("coordenadas.csv")

for i in range(len(coordenadas) - 1):
    mover_para_direcao(coordenadas[i], coordenadas[i + 1])
    time.sleep(0.5)

print("Movimentação finalizada.")
