# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 14:30:10 2021

@author: M VENKAT ANVAY REDDY
"""

from flask import Flask, request, render_template
import joblib
model = joblib.load('fourtune.save')
trans=joblib.load('scproject.save')
 
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/Prediction',methods=['POST','GET'])
def prediction():
    return render_template('indexnew.html')
@app.route('/Home',methods=['POST','GET'])
def my_home():
    return render_template('home.html')
@app.route('/predict',methods=["POST","GET"])
def predict():
    x_test=[[float(x) for x in request.form.values()]]
    x_test=trans.transform(x_test)
    y_pred=model.predict(x_test)
    output=y_pred[0]
    return render_template('resultnew.html',prediction='{}'.format(output))


if __name__== '__main__':
    app.run(debug=True)