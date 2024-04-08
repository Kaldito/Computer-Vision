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
  
# ------------------- Mostrar imagen ------------------- #  
# Se usa la función imshow para mostrar la imagen  
cv.imshow(" Image", img_gray)  
# Se usa la función waitKey para esperar a que el usuario presione una tecla para cerrar la ventana  
cv.waitKey(0)
```
