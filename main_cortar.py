# Programa para cortar imagens
# Edson F. Fumachi
# effumachi@gmail.com
from PIL import Image
import os
a=int(input('Qual o último número de arquivo? '))
for i in range(1,a+1):
    if(i<10):
        im = Image.open('00'+str(i)+'.png')
        im = im.crop((6, 168,767, 1268))  # (x1,y1,x2,y2)
        im.save('_00'+str(i)+'.png')
        os.remove('00'+str(i)+'.png')
    elif i<100:
        im = Image.open('0'+str(i)+'.png')
        im = im.crop((5, 168,767, 1267))  # (x1,y1,x2,y2)
        im.save('_0'+str(i)+'.png')
        os.remove('0'+str(i)+'.png')
    else:
        im = Image.open(''+str(i)+'.png')
        im = im.crop((5, 168,767, 1267))  # (x1,y1,x2,y2)
        im.save('_'+str(i)+'.png')
        os.remove(''+str(i)+'.png')