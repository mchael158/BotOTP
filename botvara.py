import cv2
import numpy as np
import time
from PIL import ImageGrab
import pyautogui

def encontrar_e_apertar_shift_f(imagem_referencia, threshold=0.8):
    # Captura a tela
    tela = ImageGrab.grab()
    tela_np = np.array(tela)
    tela_cinza = cv2.cvtColor(tela_np, cv2.COLOR_BGR2GRAY)

 
    imagem = cv2.imread(imagem_referencia, 0)
    if imagem is None:
        print("Erro: imagem não encontrada!")
        return


    resultado = cv2.matchTemplate(tela_cinza, imagem, cv2.TM_CCOEFF_NORMED)
    loc = np.where(resultado >= threshold)

    for pt in zip(*loc[::-1]):
        print(f"Imagem encontrada em: {pt} - pressionando Shift + F")
        pyautogui.keyDown('shift')
        pyautogui.press('f')
        pyautogui.keyUp('shift')
        break  

def iniciar_bot():
    print("Bot de detecção iniciado! Pressione Ctrl+C para encerrar.")
    while True:
        encontrar_e_apertar_shift_f("iscaa.png")
        time.sleep(1)  # Tempo entre verificações

if __name__ == "__main__":
    iniciar_bot()
