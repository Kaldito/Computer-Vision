Usaremos [[redes neuronales convolucionales]] para la detección de rostros usando la biblioteca de dlib.

**NOTA:** *Este proceso es muy pesado para la computadora, puede tomar unos cuantos minutos.*

```
import cv2 as cv  
import dlib  
  
# ------------------- IMAGE SETUP ------------------- #  
img = cv.imread('images/people2.jpg')  
  
# ------------------- FACE DETECTION ------------------- #  
cnn_detector = dlib.cnn_face_detection_model_v1("weights/mmod_human_face_detector.dat")  
detections = cnn_detector(img, 1)  
print(f"Number of faces detected: {len(detections)}")  
  
# ------------------- DRAWING RECTANGLES ------------------- #  
for i, face in enumerate(detections):  
    x1, y1, x2, y2, c = face.rect.left(), face.rect.top(), face.rect.right(), face.rect.bottom(), face.confidence  
    # - Confidence: 0.0 to 1.0 (1.0 is 100%)  
    print (f"Face {i+1} - Confidence: {c}")  
    cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)  
  
# ------------------- Mostrar imagen ------------------- #  
cv.imshow(" Image", img)  
cv.waitKey(0)
```