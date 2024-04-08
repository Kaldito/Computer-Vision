import cv2
import numpy as np

# Cargar la imagen de plantilla (patrón) y convertirla a escala de grises
template = cv2.imread('images/PATRON.jpeg', 0)
template_w, template_h = template.shape[::-1]

# Iniciar la captura de video
video_capture = cv2.VideoCapture(0)

while True:
  # Capturar fotograma por fotograma
  ret, frame = video_capture.read()

  # Convertir el marco capturado a escala de grises
  frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Lista para guardar las detecciones
  detections = []

  # Bucle sobre las escalas de la plantilla
  for scale in np.linspace(0.2, 1.0, 20)[::-1]:
    # Redimensionar la imagen de la plantilla según la escala actual
    resized_template = cv2.resize(template, None, fx=scale, fy=scale)
    r_w, r_h = resized_template.shape[::-1]

    # Si la plantilla redimensionada es más grande que el marco, saltar esta escala
    if r_w > frame_gray.shape[1] or r_h > frame_gray.shape[0]:
      continue

    # Realizar la coincidencia de plantillas con la plantilla redimensionada
    res = cv2.matchTemplate(frame_gray, resized_template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.6  # Ajusta este umbral según tus necesidades
    loc = np.where(res >= threshold)

    # Guardar las detecciones de esta escala
    for pt in zip(*loc[::-1]):
      detections.append((pt[0], pt[1], pt[0] + r_w, pt[1] + r_h))

      # Dibujar el rectángulo en el marco
      cv2.rectangle(frame, (pt[0], pt[1]), (pt[0] + r_w, pt[1] + r_h), (0, 255, 0), 2)

  # Mostrar el marco resultante
  cv2.imshow('Video', frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# Liberar la captura cuando todo esté terminado
video_capture.release()
cv2.destroyAllWindows()