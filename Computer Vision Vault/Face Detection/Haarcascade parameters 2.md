Para este ejercicio usaremos la siguiente imagen y modificaremos el código existente para eliminar los falsos positivos.

![[people2.jpg]]

# Parámetro: `minNeighbors`
`minNeighbors` determina el número mínimo de rectángulos vecinos que deben existir para retener una detección. En otras palabras, este parámetro afecta cuán rigurosos son los criterios para decidir si una detección propuesta es realmente el objeto que estás buscando (por ejemplo, un rostro).
## Funcionamiento de `minNeighbors`:

- **Rectángulos Vecinos**: Durante el proceso de detección, el algoritmo desliza una ventana sobre la imagen y evalúa si una región específica contiene el objeto de interés basándose en el clasificador (por ejemplo, Haar Cascade para detección de rostros). Para cada región positiva, se dibuja un rectángulo alrededor de la supuesta ubicación del objeto. Debido a variaciones en la imagen, como iluminación, textura y otros factores, un mismo objeto puede ser detectado múltiples veces en regiones ligeramente diferentes, resultando en varios rectángulos superpuestos.
- **Filtrado Basado en Vecindad**: `minNeighbors` sirve como un umbral para decidir cuántos de estos rectángulos vecinos (superpuestos o muy cercanos) deben existir para considerar que una detección es válida. Si el número de rectángulos que se superponen o están muy próximos en una región particular es menor que `minNeighbors`, entonces se asume que la detección es un falso positivo y se elimina. Por el contrario, si una región tiene un número de vecinos igual o mayor que `minNeighbors`, se considera una detección válida.
# Parámetro: `minSize`
El parámetro de `minSize` dicta el tamaño mínimo que tiene que tener un rectángulo detectado para poder ser marcado como positivo. **Por defecto: (30, 30).**
# Parámetro: `maxSize`
El parámetro de `maxSize` dicta el tamaño máximo que tiene que tener un rectángulo detectado para poder ser marcado como positivo.
## Incorporarlo en el código:
En este caso el valor se debe ir ajustando para eliminar los falsos positivos existentes, se suele partir con el valor de **5** y desde ahí ir ajustándolo.

Con la nueva imagen ya que no es demasiado grande no es necesario hacer un reescalado, y se tienen que ajustar los valores de `scaleFactor` y `minNeighbors`:

```
# Proyecto: face-detection-2
# ------------------- FACE DETECTOR ------------------- #  
# Se crea un objeto de la clase CascadeClassifier  
face_detector = cv.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")  
# Se usa la función detectMultiScale para detectar las caras en la imagen  
detections = face_detector.detectMultiScale(img_gray, scaleFactor=1.2, minNeighbors=7)  
print(f"Se han detectado {len(detections)} caras")
```

Para poder visualizar las areas de los rectángulos generados y así poder ajustar los valores de minSize y maxSize podemos incorporar lo siguiente al loop:

```
# ------------------- DRAW RECTANGLES ------------------- #  
for (x, y, w, h) in detections:  
    print(f"Coordenadas: w={w}, h={h}")  
    # Se usa la función rectangle para dibujar un rectángulo en la imagen  
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)  
    # Los parametros son:  
    # - la imagen,    # - las coordenadas del punto inicial,    # - las coordenadas del punto final,    # - el color (RGB),    # - y el grosor
```

### Código completo
```
import cv2 as cv  
  
# ------------------- IMAGE SETUP ------------------- #  
# Se usa la función imread para leer una imagen  
img = cv.imread("./images/people2.jpg")  
# El parametro .shape nos devuelve el tamaño de la imagen  
print(f"Tamaño original: {img.shape}")  
  
# Se usa la función cvtColor para cambiar el espacio de color de la imagen  
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # Cambia la imagen a escala de grises  
  
# ------------------- FACE DETECTOR ------------------- #  
# Se crea un objeto de la clase CascadeClassifier  
face_detector = cv.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")  
# Se usa la función detectMultiScale para detectar las caras en la imagen  
detections = face_detector.detectMultiScale(img_gray, scaleFactor=1.2, minNeighbors=7)  
print(f"Se han detectado {len(detections)} caras")  
  
# ------------------- DRAW RECTANGLES ------------------- #  
for (x, y, w, h) in detections:  
    # Se usa la función rectangle para dibujar un rectángulo en la imagen  
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)  
    # Los parametros son:  
    # - la imagen,    # - las coordenadas del punto inicial,    # - las coordenadas del punto final,    # - el color (RGB),    # - y el grosor  
# ------------------- Mostrar imagen ------------------- #  
# Se usa la función imshow para mostrar la imagen  
cv.imshow(" Image", img)  
# Se usa la función waitKey para esperar a que el usuario presione una tecla para cerrar la ventana  
cv.waitKey(0)
```