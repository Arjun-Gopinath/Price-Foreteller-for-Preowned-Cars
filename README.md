# Price-ForeTeller-For-Preowned-Cars

A machine learning based prediction model that is used to predict the price of used cars based on data given by user.
 
## Modules used

### For ML model creation

* Anaconda - (Jupyter Notebook,Scikit,Pandas,Python3,Numpy)
* LightGBM

### For creating website

* Flask
* requests
* jsonify
* Pickle
* HTML5-CSS

### Label encoding on features

#### Fuel Type

0 - CNG
1 - Diesel 
2 - Petrol
3 - LPG
4 - Electric

#### Brand Name

0 - Ambassador
1 - Audi
2 - BMW
3 - Bentley
4 - Chevrolet
5 - Datsun
6 - Fiat
7 - Force
8 - Ford
9 - Hindustan
10 - Honda
11 - Hyundai
12 - ISUZU
13 - Jaguar
14 - Jeep
15 - Lamborgini
16 - LandRover
17 - Mahindra
18 - Maruti
19 - Mercedes-Benz
20 - MiniCooper
21 - Mitsubishi
22 - Nissan
23 - OpelCorsa
24 - Porshe
25 - Renault
26 - Skoda
27 - Smart
28 - Tata
29 - Toyota
30 - Volkswagen
31 - Volvo

#### Location

0 - Mumbai
1 - Pune
2 - Chennai
3 - Coimbatore
4 - Hyderabad
5 - Jaipur
6 - Kochi
7 - Kolkata
8 - Delhi 
9 - Bangalore 
10 -Ahmedabad

#### Transmission

0 - Manual
1 - Automatic

#### Owner Type

0 - First
1 - Second
2 - Fourth & Above
3 - Third

## Steps to run .ipynb files

* Download & Install [Anaconda](https://www.anaconda.com/)
* Use Jupyter Notebook to run the file
* OR
* Use [Google Colab](https://colab.research.google.com/notebooks/) to run .ipynb files in the cloud.

## Steps for local deployment

* Open cmd
* Change directory to the place where the code is saved
* run "python app.py" to deploy locally. 

## Note:-

* If changes in dataset is made, model might give out undesirable outputs.
* Install all python modules mentioned above before running the project.
* Output.xlsx gives output after prediction based on test data.
* While using the website, try to avoid giving vague inputs as it provides wrong results.

# The site is [live](https://used-car-price-predictor.herokuapp.com/).
