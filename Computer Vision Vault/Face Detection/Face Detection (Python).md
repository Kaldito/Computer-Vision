**Proyecto:** pre-processing-image
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
detections = face_detector.detectMultiScale(img_gray)  
print(f"Se han detectado {len(detections)} caras")  
  
# ------------------- DRAW RECTANGLES ------------------- #  
for (x, y, w, h) in detections:  
    # Se usa la función rectangle para dibujar un rectángulo en la imagen  
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)  
    # Los parametros son:  
    # - la imagen,    # - las coordenadas del punto inicial,    # - las coordenadas del punto final,    # - el color (RGB),    # - y el grosor  
# ------------------- Mostrar imagen ------------------- #  
# Se usa la función imshow para mostrar la imagen  
cv.imshow(" Image", img)  
# Se usa la función waitKey para esperar a que el usuario presione una tecla para cerrar la ventana  
cv.waitKey(0)
```
NOTA: Este código cuenta con el error de detectar 6 caras en lugar de 5.

---
# .detectMultiScale()
`.detectMultiScale` es el método que se llama para detectar los rostros en la imagen. El "MultiScale" en el nombre se refiere a su capacidad de detectar rostros de diferentes tamaños en la imagen. Esto es importante porque un rostro puede aparecer más grande o más pequeño en una imagen dependiendo de qué tan cerca o lejos esté de la cámara.
## Funcionamiento
1. **Análisis en Múltiples Escalas**: Como su nombre indica, `detectMultiScale` busca rostros en varias escalas (tamaños) porque un rostro puede estar más cerca o más lejos de la cámara. Esto se hace escalando la imagen hacia abajo y buscando rostros en cada escala.
2. **Ventanas Deslizantes**: Utiliza un enfoque de ventanas deslizantes para examinar diferentes áreas de la imagen en busca de características que coincidan con las de un rostro. Cada área se evalúa con el clasificador para determinar si contiene un rostro.
3. **Detecciones y Coordenadas**: Para cada detección positiva (cuando encuentra un rostro), `detectMultiScale` registra las coordenadas del rostro en la imagen, junto con el tamaño del rostro detectado. Estos se devuelven en `detections` como una lista de rectángulos, donde cada rectángulo contiene las coordenadas `(x, y)` del vértice superior izquierdo del rostro detectado, junto con el ancho y la altura del rectángulo.


