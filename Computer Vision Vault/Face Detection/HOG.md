# ¿Qué es HOG (Histograms of Orientated Gradients)?
Imagina que tienes una fotografía y quieres que una computadora pueda reconocer objetos dentro de ella, como personas, autos o animales. Para hacer esto, la computadora necesita una manera de "entender" y describir las formas y estructuras presentes en la imagen. Aquí es donde entran en juego los HOG.

Los HOG son una técnica de visión por computadora y procesamiento de imágenes utilizada para la detección de objetos. La idea básica es bastante sencilla:
## **Gradientes de la Imagen:**
Primero, se calculan los gradientes (cambios en la intensidad o color) de la imagen. Esto se hace porque los gradientes capturan bien los contornos o bordes de los objetos en la imagen, y estos contornos son muy útiles para identificar formas.
## **Orientación de los Gradientes:** 
Luego, se mira la dirección de estos gradientes. Imagina que cada borde en la imagen es una flecha que apunta en la dirección donde el cambio es más fuerte. Estas "flechas" pueden apuntar en cualquier dirección (horizontal, vertical, diagonal, etc.).
![[Pasted image 20240317142447.png]]
## **Histogramas:** 
Ahora, se dividen la imagen en pequeñas regiones o celdas y, para cada una, se crea un histograma que cuenta cuántas "flechas" (gradientes) apuntan en cada dirección posible. Esto nos da un "perfil" de cómo son los bordes dentro de cada parte de la imagen.
![[Pasted image 20240317142555.png]]
## **Normalización:** 
Finalmente, para asegurarse de que estos histogramas sean comparables entre diferentes partes de la imagen o entre diferentes imágenes que pueden tener diferentes iluminaciones, se normalizan. Esto significa ajustar los valores para que no dependan tanto de las condiciones de luz o sombra.
![[Pasted image 20240317142807.png]]
Al final, lo que obtenemos es una representación de la imagen original que resalta sus características estructurales (formas, bordes, texturas) de una manera que las computadoras pueden procesar eficientemente. Esto es particularmente útil para tareas como la detección de peatones, donde las formas (como la silueta de una persona) son importantes para identificar el objeto de interés.
![[Pasted image 20240317143303.png]]