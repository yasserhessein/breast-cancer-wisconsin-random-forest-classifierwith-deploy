import numpy as np
import pandas as pd
from flask_cors import  cross_origin
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

@cross_origin()
@app.route('/')
def home():
    return render_template('index.html')
@cross_origin()
@app.route('/predict',methods=['POST'])
def predict():
    Sample code number = float(request.form['Sample code number'])
    Clump Thickness = float(request.form['Clump Thickness'])
    Uniformity of Cell Size = float(request.form['Uniformity of Cell Size'])
    Single Epithelial Cell Size = float(request.form['Single Epithelial Cell Size'])
    Bare Nuclei = float(request.form['Bare Nuclei'])
    Bland Chromatin = float(request.form['Bland Chromatin'])
    Normal Nucleoli = float(request.form['Normal Nucleoli'])
    Mitoses = float(request.form['Mitoses'])
    

    filename = 'm.pkl'
    loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
    scalar = pickle.load(open("m.pkl", 'rb'))
    # predictions using the loaded model file
    prediction = loaded_model.predict(scalar.transform(
        [[Sample code number, Clump Thickness ,Uniformity of Cell Size, Uniformity of Cell Shape, Marginal Adhesion,Single Epithelial Cell Size, Bare Nuclei, Bland Chromatin, Normal Nucleoli ,Mitoses]]))
    if prediction ==[1]:
            prediction = "Cancer"

    else:
            prediction = "Normal"

    # showing the prediction results in a UI
    if  prediction =="Cancer":

        return render_template('Cancer.html', prediction=prediction)
    else:
        return render_template('Normal.html',prediction=prediction)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
	#app.run(debug=True)
