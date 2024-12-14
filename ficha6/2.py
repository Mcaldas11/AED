from PIL import Image

newSize=(240,240)
imagem=Image.new(size=newSize, mode= "RGB", color="white")
pixelMap=imagem.load()
for i in range(imagem.width):
    for j in range(imagem.height):
        if j<80:
            pixelMap[i,j]=(0,0,255)
        elif j<160:
            pixelMap[i,j]=(255,255,255)
        else:
            pixelMap[i,j]=(255,0,0)
imagemRodada = imagem.rotate(90)
imagemRodada.show()