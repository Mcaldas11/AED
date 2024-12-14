from PIL import Image
from random import randint
import os

def imageArt(imagem):
    # Dimensões da imagem
    largura, altura = 400, 400
    # Criação da imagem RGB
    img = Image.new("RGB", (largura, altura))
    
    for x in range(largura):
        for y in range(altura):
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            img.putpixel((x, y), (r, g, b))
    
    if not os.path.exists("images"):
        os.makedirs("images")
    
    caminho_imagem = os.path.join("images", imagem)
    img.save(caminho_imagem)
    
    img.show()

imageArt("imageArt.jpg")
