from rembg import remove 
from PIL import Image
entrada='coala.jpg'
saida='resultado.png'
input=Image.open(entrada)
output=remove(input)
output.save(saida)