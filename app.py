from flask import Flask, render_template, request, redirect, url_for
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
file = open('lightGBM_regressor.pkl', 'rb')
# load lightGBM regression model
model = pickle.load(file)
file.close()
# Landing Page


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

# Go Back


@app.route("/predict", methods=['GET'])
def Back():
    predict_show = 0
    return redirect(url_for('Home'))


# Prediction


@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        y_pred_totlgb = []
        Location = int(request.form['Location'])

        Year = int(request.form['Year'])
        Car_Age = 2020 - Year

        Kilometers_Driven = int(request.form['Kilometers_Driven'])

        Brand = int(request.form['Brand_Name'])

        Fuel_Type = int(request.form['Fuel_Type'])

        Transmission = int(request.form['Transmission'])

        Owner_Type = int(request.form['Owner_Type'])

# Mileage

        Mileage = str(request.form['Mileage'])

        Mileage = Mileage.replace('null kmpl', '0 kmpl')

        Mileage = float(Mileage.split(' ')[0])

# Engine

        Engine = str(request.form['Engine'])

        Engine = Engine.replace('null bhp', '0 bhp')

        Engine = float(Engine.split(' ')[0])

# Power

        Power = request.form['Power']

        Power = Power.replace('null CC', '0 CC')

        Power = float(Power.split(' ')[0])

        Seats = float(request.form['Seats'])

        data = [[Location,
                 Year,
                 Kilometers_Driven,
                 Fuel_Type,
                 Transmission,
                 Owner_Type,
                 Mileage,
                 Engine,
                 Power,
                 Seats,
                 Car_Age,
                 Brand]]

        df = pd.DataFrame(data, columns=['Location',
                                         'Year',
                                         'Kilometers_Driven',
                                         'Fuel_Type',
                                         'Transmission',
                                         'Owner_Type',
                                         'Mileage',
                                         'Engine',
                                         'Power',
                                         'Seats',
                                         'Car_Age',
                                         'Brand'])
        df['Year'] = df['Year'].astype('category')

        lgbm_final = np.expm1(model.predict(df))
        output = round(lgbm_final[0], 3)
        predict_show = 1
        if output < 0:
            return render_template('./index.html', prediction_text="Sorry you cannot sell this car")
        else:
            return render_template('./index.html', prediction_text="You can sell your car at \u20B9 {} lakhs".format(output))
    else:
        return redirect(url_for('Home'))


if __name__ == "__main__":
    app.debug = True
    app.run('127.0.0.1', 8000)
