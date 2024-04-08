# Código

```
import cv2 as cv  
  
# ------------------- IMAGE SETUP ------------------- #  
# Se usa la función imread para leer una imagen  
img = cv.imread("./images/people1.jpg")  
# El parametro .shape nos devuelve el tamaño de la imagen  
print(f"Tamaño original: {img.shape}")  
  
# Se usa la función resize para cambiar el tamaño de la imagen  
img = cv.resize(img, (800, 600))  
print(f"Tamaño reducido: {img.shape}")  
  
# Se usa la función cvtColor para cambiar el espacio de color de la imagen  
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # Cambia la imagen a escala de grises  
  
# ------------------- FACE DETECTOR ------------------- #  
# Se crea un objeto de la clase CascadeClassifier  
face_detector = cv.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")  
# Se usa la función detectMultiScale para detectar las caras en la imagen  
detections = face_detector.detectMultiScale(img_gray, scaleFactor=1.09)  
print(f"Se han detectado {len(detections)} caras")  
  
# ------------------- EYE DETECTOR ------------------- #  
# Se crea un objeto de la clase CascadeClassifier  
eye_detector = cv.CascadeClassifier("./cascades/haarcascade_eye.xml")  
# Se usa la función detectMultiScale para detectar los ojos en la imagen  
eye_detections = eye_detector.detectMultiScale(img_gray)  
print(f"Se han detectado {len(eye_detections)} ojos")  
  
# ------------------- DRAW RECTANGLES (FACE) ------------------- #  
for (x, y, w, h) in detections:  
    # Se usa la función rectangle para dibujar un rectángulo en la imagen  
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)  
    # Los parametros son:  
    # - la imagen,    # - las coordenadas del punto inicial,    # - las coordenadas del punto final,    # - el color (RGB),    # - y el grosor  
# ------------------- DRAW RECTANGLES (EYE) ------------------- #  
for (x, y, w, h) in eye_detections:  
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)  
  
# ------------------- Mostrar imagen ------------------- #  
# Se usa la función imshow para mostrar la imagen  
cv.imshow(" Image", img)  
# Se usa la función waitKey para esperar a que el usuario presione una tecla para cerrar la ventana  
cv.waitKey(0)
```

## Resultado
![[Pasted image 20240317134703.png]]
# Optimización
Para eliminar los falsos positivos de la imagen se tienen que hacer varios ajustes al código inicial.

Primero que nada tenemos que eliminar el `resize` de la imagen, ya que trabajar sobre el tamaño real de la imagen nos da mas definición y el modelo de reconocimiento puede trabajar mejor. Al hacer esto podemos observar como saltaran falsos positivos tanto de los ojos como de las caras.

Ya que estamos trabajando sobre el tamaño real de la imagen hay que ajustar los valores de los parámetros `scaleFactor`, `minNeighbors`, `minSize` y `maxSize`.

En el caso del detector de rostros se tiene que ajustar el `scaleFactor` a un valor mas grande ya que estamos trabajando con la escala real de la imagen y no hay necesidad de ser tan minuciosos en la búsqueda, esto elimina casi todos los falsos positivos pero quedara un pequeño rectángulo apuntando a la nada, como podemos observar que el tamaño es bastante mas chico que el resto podemos ajustar el valor `minSize` para eliminarlo.

```
detections = face_detector.detectMultiScale(img_gray, scaleFactor=1.3, minSize=(30, 30))
```

Y en el caso del detecto de ojos dejaremos el valor por defecto de `scaleFactor` (1.1) ya que todos los ojos son detectados, pero ajustaremos el valor de `minNeighbors` para necesitar mas validaciones al detectar un ojo, también eliminaremos la falsa detección del rectángulo mas grande que el resto con el parámetro `maxSize`.

```
eye_detections = eye_detector.detectMultiScale(img_gray, minNeighbors=10, maxSize=(75, 75))
```