```
from PIL import Image  
import cv2  
import numpy as np  
import zipfile  
  
path = "./datasets/yalefaces.zip"  
zip_object = zipfile.ZipFile(file=path, mode="r")  
zip_object.extractall("./")  
zip_object.close()
```

En este código cargamos el banco de datos principal a python y descomprimimos e zip mediante código.
