#Edson F. Fumachi
#effumachi@gmail.com
from fpdf import FPDF
from os import listdir
path = "./prints/"
imagelist = listdir(path)
pdf = FPDF()
# imagelist is the list with all image filenames
x,y,w,h = 0,0,250,210       # x,y,x+dx,y+dy
for image in imagelist:
    pdf.add_page('L')
    pdf.image(path+image,x,y,w,h)
pdf.output("livro.pdf", "F")