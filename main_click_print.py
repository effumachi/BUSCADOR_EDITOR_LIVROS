# Programa para clicar em uma região especifica
# do monitor após um determinado tempo e tirar print da tela.
# Edson F. Fumachi
# effumachi@gmail.com
import pyautogui
import msvcrt
import time
a=int(input("Quantas paginas o livro tem?\n\n*Não esquecer da capa, contracapa, etc!\n\nInsira os números aqui: "))
time.sleep(5)
for i in range(1,a+1):
    if i<10:
        pic = pyautogui.screenshot()
        pic.save("00"+str(i)+".png")
    elif i<100:
        pic = pyautogui.screenshot()
        pic.save("0"+str(i)+".png")
    else:
        pic = pyautogui.screenshot()
        pic.save(''+str(i)+".png")
    pyautogui.click(760, 650, button='left')    # Configuração para tela inclinada
    #pyautogui.click(1350, 380, button='left')    # Configuração para tela normal
    time.sleep(10)