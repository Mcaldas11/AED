from PIL import Image

def imageGrayScale(input_image_path):
    # Abrir a imagem de entrada
    image = Image.open(input_image_path)
    
    # Obter as dimensões da imagem
    width, height = image.size
    
    # Criar uma nova imagem em modo "L" (grayscale)
    grayscale_image = Image.new("L", (width, height))
    
    # Converter cada pixel da imagem original para grayscale usando a fórmula NTSC
    for x in range(width):
        for y in range(height):
            # Obter os valores RGB do pixel atual
            red, green, blue = image.getpixel((x, y))
            
            # Aplicar a fórmula NTSC para calcular o valor de cinza
            gray = int(0.299 * red + 0.587 * green + 0.114 * blue)
            
            # Definir o valor do pixel em grayscale
            grayscale_image.putpixel((x, y), gray)
    
    # Mostrar a imagem em grayscale
    grayscale_image.show()


imageGrayScale("ficha6/images/img1.jpg")
