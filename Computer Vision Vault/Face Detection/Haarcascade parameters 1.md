# Parámetro: scaleFactor
## Reducción de Escala
Imagina que estás buscando rostros en una imagen. Estos rostros pueden variar en tamaño: algunos pueden estar cerca de la cámara y aparecer grandes, mientras que otros pueden estar lejos y verse pequeños. Para asegurarnos de detectar rostros de diferentes tamaños, podemos buscar repetidamente en la imagen en diferentes escalas, es decir, reduciendo gradualmente el tamaño de la imagen y buscando rostros en cada versión reducida. **Por Defecto: 1.1.**
## ¿Cómo Funciona `scaleFactor`?

- **Escala de la Imagen**: `scaleFactor` determina cuánto se reduce el tamaño de la imagen en cada paso de la escala. Por ejemplo, un `scaleFactor` de 1.1 indica que en cada paso, la imagen se reduce en un 10%, haciéndola progresivamente más pequeña.
- **Balance entre Precisión y Rendimiento**: Un `scaleFactor` pequeño, como 1.01, significa que la reducción entre escalas es mínima, lo que permite detectar rostros más pequeños pero aumenta el número de pasos de escala y, por lo tanto, el tiempo de procesamiento. Por otro lado, un valor más grande, como 1.5, reduce significativamente la imagen en cada paso, lo que puede hacer que la detección sea más rápida pero a costa de posiblemente perder rostros pequeños.
- **Detección de Rostros en Diferentes Tamaños**: Al ajustar `scaleFactor`, el algoritmo puede ser más eficiente en encontrar rostros de diferentes tamaños. Esto es especialmente útil en imágenes donde los rostros pueden variar mucho en tamaño debido a su distancia con respecto a la cámara.
## Incorporarlo en el código
Al incorporar el parámetro de scaleFactor e ir ajustando su valor podremos eliminar los falsos positivos que daba el procesado. En este caso el valor ideal fue de **1.09**.

**Proyecto:** pre-processing-image
```
# ------------------- FACE DETECTOR ------------------- #  
# Se crea un objeto de la clase CascadeClassifier  
face_detector = cv.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")  
# Se usa la función detectMultiScale para detectar las caras en la imagen  
detections = face_detector.detectMultiScale(img_gray, scaleFactor=1.09)  
print(f"Se han detectado {len(detections)} caras")
```
