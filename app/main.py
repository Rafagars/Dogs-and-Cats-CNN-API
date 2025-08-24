import os
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

#Cargar el modelo
interpreter = tf.lite.Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()

#Obtener los tensores de entrada y salida
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
input_shape = input_details[0]['shape']

#Preprocesamiento de la imagen para la prediccion
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(input_shape[1], input_shape[2]))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img, array, axis=0)
    img_array /= 255.0 #Normalizacion
    
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonofy({'error': 'No file part'})
    file = request.file['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        img_path = 'temp.jpg'
        file.save(img_path)
        
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

if __name__ == '__main__':
    app.run(debug=True)