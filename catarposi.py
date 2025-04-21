import pyautogui
import time

print("Passe o mouse e observe:")
time.sleep(5)
while True:
    print(pyautogui.position())
    time.sleep(1)
