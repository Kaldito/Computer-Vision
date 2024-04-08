# Entrenar al modelo
```
# --- MAIN --- #  
def main():  
    # --- PREPROCESAMIENTO DE DATOS --- #  
    ids, faces = get_image_data()  
    # ids es un array con los ids de las imagenes  
    # faces es un array los pixeles de las imagenes en escala de grises (numpy array)  
    # Es importante que todas las imagenes sean del mismo tamaño y esten en     escala de grises para que funcione el    
    # algoritmo  
    
    # --- ENTRENAMIENTO --- #    
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # Crear el modelo  
    recognizer.train(faces, ids)  # Entrenar el modelo  
    # Guardar el modelo en formato .yml por que es el formato que reconoce OpenCV    
    recognizer.write("lbph_classifier.yml")  
  
  
if __name__ == '__main__':  
    main()
```

En el siguiente código entrenamos al modelo con las imágenes de entrenamiento y generamos el modelo en formato .yml.