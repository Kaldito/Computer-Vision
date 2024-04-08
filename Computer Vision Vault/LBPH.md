# Local Binary Patterns Histograms
LBPH es un método utilizado para el reconocimiento facial. Este enfoque se basa en el concepto de patrones binarios locales, que son patrones específicos encontrados en una imagen que pueden ser utilizados para describir las características visuales de dicha imagen. El método LBPH es especialmente útil para reconocer rostros en condiciones variables de iluminación y con diferentes expresiones faciales.
## Proceso

1. **División de la Imagen**: La imagen del rostro se divide en pequeñas regiones. Estas regiones se analizan individualmente, lo que permite que el algoritmo maneje diferentes características faciales de manera local.
2. **Cálculo de Patrones Binarios Locales (LBP)**: Para cada región, se calcula el LBP. Esto implica comparar cada píxel con sus vecinos cercanos. Si el valor del píxel central es menor que el de sus vecinos, se asigna un 0; si es mayor o igual, se asigna un 1. Este proceso se repite para todos los píxeles, generando un patrón binario para cada uno.
3. **Histogramas de LBP**: Se calcula un histograma de los patrones binarios obtenidos para cada región de la imagen. Estos histogramas representan la distribución de los patrones binarios dentro de una región específica y sirven como una característica distintiva para el reconocimiento facial.
4. **Comparación y Reconocimiento**: Para identificar un rostro, se compara el histograma de LBP de la imagen desconocida con los histogramas de LBP de las imágenes conocidas almacenadas en una base de datos. La comparación se realiza utilizando una medida de distancia (como la distancia euclidiana o Chi-cuadrado) para determinar cuál de las imágenes conocidas se parece más a la imagen desconocida.
5. **Resultado**: Basándose en la comparación de histogramas, el sistema puede reconocer a la persona en la imagen desconocida, asumiendo que su rostro está almacenado en la base de datos.

![[Pasted image 20240331193144.png]]
![[Pasted image 20240331193153.png]]
