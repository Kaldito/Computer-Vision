Usaremos la biblioteca de dlib para poder usar la tecnica HOG para deteccion de rostros.

```
import cv2 as cv  
import dlib  
  
# ------------------- IMAGE SETUP ------------------- #  
img = cv.imread('images/people2.jpg')  
  
# ------------------- FACE DETECTION ------------------- #  
face_detector_hog = dlib.get_frontal_face_detector()  
# - Usamos el detector de rostros HOG para detectar rostros en la imagen  
# - El segundo argumento es el número de veces que se debe aumentar la imagen  
#   antes de ejecutar la detección. Usamos 1 para la imagen original.  
detections = face_detector_hog(img, 1)  
print(f"Number of faces detected: {len(detections)}")  
  
# ------------------- DRAWING RECTANGLES ------------------- #  
for face in detections:  
    x, y, w, h = face.left(), face.top(), face.width(), face.height()  
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  
  
# ------------------- Mostrar imagen ------------------- #  
cv.imshow(" Image", img)  
cv.waitKey(0)
```