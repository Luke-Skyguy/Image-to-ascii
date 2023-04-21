import argparse
import numpy as np 
from PIL import Image

from methods import getAverageL, turnToAscii
# valores de nivel de escala de grises.
# 70% gris

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
