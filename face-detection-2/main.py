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
    print(f"Coordenadas: w={w}, h={h}")
    # Se usa la función rectangle para dibujar un rectángulo en la imagen
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Los parametros son:
    # - la imagen,
    # - las coordenadas del punto inicial,
    # - las coordenadas del punto final,
    # - el color (RGB),
    # - y el grosor

# ------------------- Mostrar imagen ------------------- #
# Se usa la función imshow para mostrar la imagen
cv.imshow(" Image", img)
# Se usa la función waitKey para esperar a que el usuario presione una tecla para cerrar la ventana
cv.waitKey(0)
