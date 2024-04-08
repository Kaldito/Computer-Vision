```
# --- ENTRENAMIENTO --- #  
# recognizer = cv2.face.LBPHFaceRecognizer_create()  # Crear el modelo  
# recognizer.train(faces, ids)  # Entrenar el modelo  
# # Guardar el modelo en formato .yml por que es el formato que reconoce OpenCV  
# recognizer.write("lbph_classifier.yml")  
  
# --- RECONOCER ROSTROS --- #  
lbph_classifier = cv2.face.LBPHFaceRecognizer_create()  
lbph_classifier.read("./lbph_classifier.yml")  
  
image = convert_image_to_array("./yalefaces/test/subject10.sad.gif")  
  
# --- PREDICCION --- #  
prediction = lbph_classifier.predict(image)  
  
# --- VISUALIZACION --- #  
expected_output = int(os.path.split("./yalefaces/test/subject10.sad.gif")[1].split(".")[0].replace("subject", ""))  
  
cv2.putText(image, f"P: {prediction[0]}", (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)  
cv2.putText(image, f"E: {expected_output}", (10, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)  
cv2.imshow("LBPH Classifier", image)  
  
cv2.waitKey(0)
```
