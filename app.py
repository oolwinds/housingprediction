import json
import pickle
from flask import Flask, app,jsonify, url_for,render_template,redirect,flash,session,escape,request
import numpy as np
import pandas as pd

app=Flask(__name__)
#Load the model
regmodel = pickle.load(open('regmodel.pkl','rb'))
scaler = pickle.load(open('scaling.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scaler.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)[0]
    return render_template("home.html", prediction_text="The price of the house is estimated to be ${:,.0f}000".format(output))


if __name__=="__main__":
    app.run(debug=True)