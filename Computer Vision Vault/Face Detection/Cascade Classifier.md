# ¿Qué es?
El **Cascade Classifier** es un algoritmo diseñado para detectar objetos en una imagen de manera eficiente. Imagínalo como un filtro rápido que pasa por diferentes etapas, donde cada etapa decide si un área de la imagen es o no el objeto que está buscando. Este proceso se llama *"cascade"* porque la información fluye a través de múltiples etapas de clasificación, como una cascada.

Aquí está cómo funciona de manera sencilla:
## **Preparación**
Antes de poder detectar objetos, el clasificador debe ser entrenado con muchas imágenes del objeto que queremos detectar (por ejemplo, rostros humanos) y muchas imágenes de lo que no es ese objeto. Durante el entrenamiento, el algoritmo aprende características distintivas del objeto
## Detección
Cuando se utiliza el clasificador entrenado para detectar objetos en nuevas imágenes, la imagen se examina en pequeñas áreas o ventanas.
## Etapas de la cascada
Cada área pasa por varias etapas de clasificadores. En cada etapa, el algoritmo verifica si esa área contiene alguna característica del objeto. Si una etapa determina que es poco probable que el área contenga el objeto, se descarta, y el algoritmo no procesa esa área en etapas más detalladas. Esto hace que el proceso sea muy eficiente, ya que solo las áreas más prometedoras pasan a través de todas las etapas.

![[Pasted image 20240316231630.png]]
## Resultado
Al final del proceso, las áreas que pasan todas las etapas se consideran detecciones del objeto.
![[Pasted image 20240316231900.png]]
