from flask import Flask, jsonify,request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import pickle
import numpy as np

app = Flask(__name__)
cors = CORS(app)

model = pickle.load(open("class.pkl", "rb"))

app.config['UPLOAD_FOLDER'] = 'D:\\Kaarproject\\ammu'

@app.route('/form', methods=['POST'])
def pred_form():
    QUANTITYORDERED = request.json['QUANTITYORDERED']
    PRICEEACH = request.json['PRICEEACH']
    MONTH_ID = request.json['MONTH_ID']
    YEAR_ID = request.json['YEAR_ID']
    DEALSIZE = request.json['DEALSIZE']
    data = [int(QUANTITYORDERED), int(PRICEEACH), int(MONTH_ID), int(YEAR_ID), int(DEALSIZE)]
    data = [np.array(data)]
    predict = model.predict(data)
    return jsonify(predict.tolist())

@app.route('/upload', methods=['POST'])
def handle_file():
  if 'file' not in request.files:
    return jsonify({'error': 'No file included in request.'}), 400
    
  file = request.files['file']
    
  if file.filename == '':
    return jsonify({'error': 'No file selected.'}), 400
    
  if file and allowed_file(file.filename):
    # Save the file
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    return jsonify({'message': 'File uploaded successfully.'}), 200
  else:
    return jsonify({'error': 'Invalid file format.'}), 400
    
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'txt', 'xls', 'csv'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
