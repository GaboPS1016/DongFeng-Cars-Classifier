import os
import numpy as np
from PIL import Image

# CONFIGURACIÓN
CARPETA_RAIZ = "dataset_dongfeng"
TAMAÑO_IMG = (224, 224)          # tamaño de redimensionado
ARCHIVO_SALIDA = "carros_dongfeng.npz"

# Obtener clases = subcarpetas ordenadas
clases = sorted(os.listdir(CARPETA_RAIZ))
print(f"Clases: {clases}")

imagenes = []
etiquetas = []

for idx, clase in enumerate(clases):
    ruta_clase = os.path.join(CARPETA_RAIZ, clase)
    if not os.path.isdir(ruta_clase):
        continue

    for archivo in os.listdir(ruta_clase):
        if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.webp')):
            ruta_img = os.path.join(ruta_clase, archivo)
            try:
                # Cargar en escala de grises ('L') y redimensionar
                img = Image.open(ruta_img).convert('L')
                img = img.resize(TAMAÑO_IMG)
                arr = np.array(img, dtype=np.uint8)   # forma (224, 224)

                imagenes.append(arr)
                etiquetas.append(idx)
            except Exception as e:
                print(f"Error con {ruta_img}: {e}")

# Convertir a arrays numpy
X = np.array(imagenes)          # (N, 224, 224)
y = np.array(etiquetas)         # (N,)

print(f"Total imágenes: {len(X)}")
print(f"Forma de X: {X.shape}, Forma de y: {y.shape}")

# Guardar comprimido
np.savez_compressed(ARCHIVO_SALIDA,
                    images=X,
                    labels=y,
                    class_names=clases)
print(f"Dataset guardado en {ARCHIVO_SALIDA}")