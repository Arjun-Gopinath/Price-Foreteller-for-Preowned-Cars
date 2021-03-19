from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# load lightGBM regression model
model = pickle.load(open('lightGBM_regressor.pkl', 'rb'))

# Landing Page


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

# Page after prediction


@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':

        Location = int(request.form['Location'])

        Year = int(request.form['Year'])
        Car_Age = 2020 - Year

        Kilometers_Driven = int(request.form['Kilometers_Driven'])

        Fuel_Type = int(request.form['Fuel_Type'])

        Transmission = int(request.form['Transmission'])

        Owner_Type = str(request.form['Owner_Type'])

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

        Price = float(request.form['Price'])

        prediction = model.predict([
            [Location,
             Year,
             Kilometers_Driven,
             Fuel_Type,
             Transmission,
             Owner_Type,
             Mileage,
             Engine,
             Power,
             Seats,
             Car_Age]])

        output = round(prediction[0], 2)
        if output < 0:
            return render_template('index.html', prediction_text="Sorry you cannot sell this car")
        else:
            return render_template('index.html', prediction_text="You can sell your car at \u20B9 {} lakhs".format(output))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
