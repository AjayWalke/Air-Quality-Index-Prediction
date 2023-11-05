# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__) 


@app.route('/')
def home():
    return render_template('index.html')

# T annual temperature
# TM maximum temperature
# Tm minimum temperature
# SLP sea level pressure
# H humidity
# VV visibility
# V wind speed
# VM Maximum Sustained Wind Speed

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        city = request.form['city']
        t = int(request.form['T'])
        tm = int(request.form['TM'])
        tmm = int(request.form['Tm'])
        slp = int(request.form['SLP'])
        h = int(request.form['H'])
        vv = float(request.form['VV'])
        v = float(request.form['V'])
        vm = int(request.form['VM'])
        ans = []
        if(city == 'pune'):
            print(1)
            filename = './pkl_files/Pune.pkl'
            classifier = pickle.load(open(filename, 'rb'))
            data = np.array([[t, tm, tmm, slp, h, vv, v, vm]])
            my_prediction = classifier.predict(data)
            ans.insert(my_prediction)
        elif(city == 'nagpur'):
            print(2)
            filename = './pkl_files/Nagpur.pkl'
            classifier = pickle.load(open(filename, 'rb'))
            data = np.array([[t, tm, tmm, slp, h, vv, v, vm]])
            my_prediction = classifier.predict(data)
            ans.insert(my_prediction)
        elif(city == 'delhi'):
            print(3)
            filename = './pkl_files/Delhi.pkl'
            classifier = pickle.load(open(filename, 'rb'))
            data = np.array([[t, tm, tmm, slp, h, vv, v, vm]])
            my_prediction = classifier.predict(data)
            ans.insert(my_prediction)
        elif(city == 'mumbai'):
            print(4)
            filename = './pkl_files/Mumbai.pkl'
            classifier = pickle.load(open(filename, 'rb'))
            data = np.array([[t, tm, tmm, slp, h, vv, v, vm]])
            my_prediction = classifier.predict(data)
            ans.insert(my_prediction)
        elif(city == 'chennai'):
            print(4)
            filename = './pkl_files/Chennai.pkl'
            classifier = pickle.load(open(filename, 'rb'))
            data = np.array([[t, tm, tmm, slp, h, vv, v, vm]])
            my_prediction = classifier.predict(data)
            ans.insert(my_prediction)
        elif(city == 'bangalore'):
            print(5)
            filename = './pkl_files/Bangalore.pkl'
            classifier = pickle.load(open(filename, 'rb'))
            data = np.array([[t, tm, tmm, slp, h, vv, v, vm]])
            my_prediction = classifier.predict(data)
            ans.insert(my_prediction)

        print(ans);
        return render_template('result.html', prediction=ans)


if __name__ == '__main__':
    app.run(debug=True)
