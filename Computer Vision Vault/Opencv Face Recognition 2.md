# Preprocesamiento de datos
```
from PIL import Image  
import cv2  
import numpy as np  
import zipfile  
import os  
  
# --- CARGAR IMAGENES DE UNA CARPETA --- #  
# path_zip = "./datasets/yalefaces.zip"  
# zip_object = zipfile.ZipFile(file=path_zip, mode="r")  
# zip_object.extractall("./")  
# zip_object.close()  
  
# --- CONSTANTES --- #  
PATH_TRAIN = "./yalefaces/train"  
  
  
# --- OBTENER IMAGENES DE UNA CARPETA --- #  
def get_image_data():  
    paths = [os.path.join(PATH_TRAIN, f) for f in os.listdir(PATH_TRAIN)]  
  
    faces = []  
    ids = []  
  
    for path in paths:  
        image = Image.open(path).convert('L') # Convertir a escala de grises  
        image_np = np.array(image, 'uint8') # Convertir a numpy array de 8 bits  
  
        image_id = int(os.path.split(path)[1].split(".")[0].replace("subject", ""))  
        ids.append(image_id)  
        faces.append(image_np)  
  
    return np.array(ids), faces  
  
  
# --- MAIN --- #  
def main():  
    # --- PREPROCESAMIENTO DE DATOS --- #  
    ids, faces = get_image_data()  
    # ids es un array con los ids de las imagenes  
    # faces es un array los pixeles de las imagenes en escala de grises (numpy array)  
    # Es importante que todas las imagenes sean del mismo tamaño y esten en escala de grises para que funcione el    # algoritmo  
  
if __name__ == '__main__':  
    main()
```