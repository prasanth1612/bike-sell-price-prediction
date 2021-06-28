import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math
app = Flask(__name__)
model = pickle.load(open('reg.pkl', 'rb'))

@app.route('/',methods=['GET'])
def home():
    return render_template("app.html")
  

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        mileage = float(request.form['mileage'])
        age = float(request.form['age'])
        prediction = model.predict([[mileage,age]])
        
        output = math.floor(prediction)
        if output<0:
            return render_template('app.html',prediction_text='Sorry you cannot sell your bike')
		
        else:
            return render_template('app.html',prediction_text=float(output))

if __name__ == "__main__":
    app.run(debug=True)
