# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 08:20:59 2021

@author: ADMIN
"""
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os

os.chdir('D://my project')
app = Flask(__name__,template_folder='template')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def home():
    return render_template("app.html")

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        mileage = float(request.form['mileage'])
        age = float(request.form['Weight'])
        prediction = model.predict([[mileage,age])
        
        output = prediction
        if output=='f':
            return render_template('app.html',prediction_text='you are female!')
		
        else:
            return render_template('app.html',prediction_text='you are male!')

if __name__ == "__main__":
    app.run(debug=True)
