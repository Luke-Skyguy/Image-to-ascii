import sys,math,argparse,random
import numpy as np 
from PIL import Image

# valores de nivel de escala de grises.
# 70% gris
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# 10% gris
gscale2 = '@%#*+=-:. '

def getAverageL(imagen):
    """
    Dada la imagen PIL, devuelve el valor promedio de escala de grises
    """
    # obtener imagen como arreglo numpy
    im = np.array(imagen)
 
    # obtener forma
    
    w,h = im.shape
 
    # obtener promedio
    return np.average(im.reshape(w*h))
   
#Dada la imagen y las dimensiones (filas, columnas) devuelve una lista de imágenes m*n
def turnToAscii(nombreArchivo, columnas, escala, moreLevels):
    
    # declarar variables globales
    global gscale1, gscale2
 
    # abrir imagen y convertir a escala de grises
    imagen = Image.open(nombreArchivo).convert('L')
 
    # guardar dimensiones
    W, H = imagen.size[0], imagen.size[1]
    print("Dimensiones de la imagen de entrada: %d x %d" % (W, H))
 
    # calcular ancho de la sección
    w = W/columnas
 
    # calcular altura de la sección basada en la relación de aspecto y la escala
    h = w/escala * 0.75
 
    # calcular número de filas
    filas = int(H/h)
     
    print("Columnas: %d, Filas: %d" % (columnas, filas))
    print("Dimensiones de la sección: %d x %d" % (w, h))
 
    # verificar si el tamaño de la imagen es demasiado pequeño
    if columnas > W or filas > H:
        print("¡Imagen demasiado pequeña para las columnas especificadas!")
        exit(0)
 
    # la imagen ASCII es una lista de cadenas de caracteres
    imagenASCII = []
    # generar lista de dimensiones
    for j in range(filas):
        y1 = int(j*h)
        y2 = int((j+1)*h)
 
        # corregir última sección
        if j == filas-1:
            y2 = H
 
        # agregar una cadena vacía
        imagenASCII.append("")
 
        for i in range(columnas):
 
            # recortar imagen a la sección
            x1 = int(i*w)
            x2 = int((i+1)*w)
 
            # corregir última sección
            if i == columnas-1:
                x2 = W
 
            # recortar imagen para extraer la sección
            ImagenSelecc = imagen.crop((x1, y1, x2, y2))
 
            # obtener iluminacion promedio
            promedio = int(getAverageL(ImagenSelecc))
            if moreLevels:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]

# Agrega el carácter ASCII a la cadena
            imagenASCII[j] += gsval

# Devuelve la imagen en formato de texto
            return imagenASCII


# Función main()
def main():
    # Especifica las condiciones de los argumentos
    descStr = "Convierte tu imagen a ASCII."
    parser = argparse.ArgumentParser(description=descStr)

    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels',dest='moreLevels',action='store_true')

    # Analiza los argumentos
    args = parser.parse_args()

    imgFile = args.imgFile

    # Define el archivo de salida
    outFile = 'out.txt'
    if args.outFile:
        outFile = args.outFile

    # Establece la escala
    scale = 0.43
    if args.scale:
        scale = float(args.scale)

    # Establece las columnas
    cols = 80
    if args.cols:
        cols = int(args.cols)

    print('generando arte ASCII...')
    # Convierte la imagen en texto ASCII
    aimg = turnToAscii(imgFile, cols, scale, args.moreLevels)

    # Abre el archivo
    f = open(outFile, 'w')

    # Escribe en el archivo
    for row in aimg:
        f.write(row + '\n')

    f.close()
    print("Arte ASCII escrito en %s" % outFile)

if __name__ == '__main__':
    main()       
