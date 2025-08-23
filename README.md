# 🐶 Clasificador de Perros y Gatos con API en Flask 🐱

## 📝 Resumen del Proyecto

Este proyecto es una demostración completa del ciclo de vida de un modelo de Machine Learning, desde su creación y entrenamiento hasta su despliegue como una **API web funcional**. El objetivo es clasificar imágenes como "perro" o "gato" utilizando una **Red Neuronal Convolucional (CNN)**.

La solución se divide en dos partes principales:
1.  **Modelo de Machine Learning:** Un Jupyter Notebook que documenta la creación, el entrenamiento y la evaluación del modelo.
2.  **API de Despliegue:** Un servicio web desarrollado con **Flask** que expone el modelo para recibir imágenes y devolver predicciones en tiempo real.

## ✨ Características Principales

* **Modelo CNN:** Arquitectura personalizada, entrenada para reconocer patrones en imágenes de perros y gatos.
* **Aumento de Datos:** Se utilizaron técnicas de `Data Augmentation` para mejorar la robustez y la capacidad de generalización del modelo.
* **Evaluación del Modelo:** Se usaron métricas como la **precisión**, la **exhaustividad** y la **matriz de confusión** para validar el rendimiento del modelo.
* **API en Flask:** Se creó una API RESTful simple y eficiente para interactuar con el modelo.
* **Serialización del Modelo:** El modelo final fue guardado en un archivo `.h5` (o `.tflite` para optimización) para su fácil carga y uso en la API.

## 🛠️ Tecnologías y Librerías

* **Python:** Lenguaje de programación principal.
* **TensorFlow & Keras:** Para el desarrollo y entrenamiento del modelo CNN.
* **Flask:** Para la creación del servidor web (API).
* **Jupyter Notebook:** Para el análisis, la experimentación y la documentación del modelo.
* **Numpy, Matplotlib, scikit-learn:** Librerías para el manejo de datos, visualización y evaluación.

## 🚀 Cómo Usar el Repositorio

### **Parte 1: El Modelo (en el Notebook)**

Para entender la lógica del modelo y ver el proceso de entrenamiento y evaluación:

1.  Abre el archivo `clasificador_perros_gatos.ipynb` en Google Colab o Jupyter.
2.  Sigue las instrucciones en el notebook para descargar el dataset y ejecutar cada celda.

### **Parte 2: La API (con Flask)**

Para ejecutar la API y probar el modelo en un entorno de servidor:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/tu-usuario/nombre-del-repo.git)
    cd nombre-del-repo
    ```

2.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ejecuta la API:**
    ```bash
    flask run
    ```
    La API estará disponible en `http://127.0.0.1:5000` (o el puerto que configure Flask).

4.  **Haz una predicción (ejemplo con `curl`):**
    ```bash
    curl -X POST -F "file=@/ruta/a/tu/imagen.jpg" [http://127.0.0.1:5000/predict](http://127.0.0.1:5000/predict)
    ```

## 📊 Resultados de la Evaluación


* **Gráficas de Entrenamiento:** Se incluyen gráficas en el notebook que muestran el rendimiento a lo largo de las épocas, evidenciando un rendimiento sólido.
  <img width="502" height="547" alt="image" src="https://github.com/user-attachments/assets/3e0511c9-dcda-45f3-82e9-0a06730d1733" />
  <img width="349" height="455" alt="image" src="https://github.com/user-attachments/assets/43344909-1ec9-4a01-a2b7-37e81d73f6a9" />


* **Matriz de Confusión:** El modelo mostró un rendimiento equilibrado, con un bajo número de errores tanto para perros como para gatos.
<img width="658" height="547" alt="image" src="https://github.com/user-attachments/assets/28f0fbaa-3083-425c-abf9-69eee3f97f1c" />
* **Distribuccion de Probabilidades de Prediccion**
  <img width="841" height="547" alt="image" src="https://github.com/user-attachments/assets/82e9b24a-8aea-4219-90a6-0d1d01f89fe0" />


## ✍️ Autor

* **[Rafael Garcia]** - [https://www.linkedin.com/in/rafael-garcia-sanchez-2297b816a/]

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE.md](LICENSE.md).

---
