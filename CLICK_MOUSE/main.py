# Programa para clicar em uma região especifica
# do monitor após um determinado tempo!
# Edson F. Fumachi
# effumachi@gmail.com
import pyautogui
import msvcrt
import time
a=int(input("Quantas paginas o livro tem?\n\nInsira os números aqui: "))
time.sleep(5)
for i in range(1,a+1):
    time.sleep(20)
    #Print da capa
    if i<10:
        pic = pyautogui.screenshot()
        pic.save("00"+str(i)+".png")
    #elif i<10:
    #    pic = pyautogui.screenshot()
    #    pic.save("00"+str(i)+".png")
    elif i>=10:
        pic = pyautogui.screenshot()
        pic.save("0"+str(i)+".png")
    else:
        pic = pyautogui.screenshot()
        pic.save(""+str(i)+".png")
    pyautogui.click(1350, 500, button='left')