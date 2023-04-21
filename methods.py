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
