import os
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Obtiene la ruta de la carpeta donde está main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construye la ruta al modelo subiendo un nivel y entrando a 'model'
model_path = os.path.join(BASE_DIR, '..', 'model', 'catsdogs_cnn.tflite')

# Cargamos el modelo
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

#Obtener los tensores de entrada y salida
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
input_shape = input_details[0]['shape']

# Extensiones de imagen permitidas
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

def allowed_file(filename):
    # Verifica si el archivo tiene extensión y si esta es válida
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Preprocesamiento de la imagen para la prediccion
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(input_shape[1], input_shape[2]))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0 #Normalizacion
    
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonofy({'error': 'No file part'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        img_path = 'temp.jpg'
        file.save(img_path)
        
        try:
            processed_img = preprocess_image(img_path)

            #Establecer el tensor de entrada
            interpreter.set_tensor(input_details[0]['index'], processed_img)

            #Ejecutar la inferencia
            interpreter.invoke()

            #Obtener el resultado de la inferencia
            output_data = interpreter.get_tensor(output_details[0]['index'])
            prediction = output_data[0][0]

            if prediction > 0.5:
                result = 'Perro'
                probability = float(prediction)
            else:
                result = 'Gato'
                probability = 1.0 - float(prediction)
            os.remove(img_path)
            return jsonify({'prediction': result, 'probability': probability})
        except Exception as e:
            os.remove(img_path)
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Format not Allowed'}), 400

if __name__ == '__main__':
    app.run(debug=True)
