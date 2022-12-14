from joblib import load
import numpy as np 
from flask import Flask, render_template, request

################################################
# Flask Set up
################################################

app = Flask(__name__)

################################################
# Load the Airbnb Model
################################################

model = load(open('./Models/random_forest_model_8.joblib', "rb"))

#create route that renders index template
@app.route('/')
def main():

    inputs = {"clean": ""}

    prediction_text = ""

    return render_template('index.html', result = prediction_text, form_inputs = inputs)

@app.route("/send", methods=["POST"])
def send():

    # obtain form inputs from the dataframe for running the model
    clean = float(request.form["cleanliness"])
    host = float(90)
    comms = float(5)
    loc = float(5)
    inst = float(request.form["instant"])
    short = float(request.form["short"])
    check = float(5)
    value = float(request.form["review_score_value"])
    accom = float(request.form["accomm"])
    bedrooms = float(request.form["bedrooms"])
    score = float(request.form["review_score_rating"])
    buroughs = request.form["buroughs"]
    room_type = request.form["room_type"]

    inputs = {"clean": clean}

    if buroughs == "Bronx":
        encoded_burough = [1,0,0,0,0]
    elif buroughs == "Brooklyn":
        encoded_burough = [0,1,0,0,0]
    elif buroughs == "Manhattan":
        encoded_burough = [0,0,1,0,0]
    elif buroughs == "Queens":
        encoded_burough = [0,0,0,1,0]
    elif buroughs == "Staten Island":
        encoded_burough = [0,0,0,0,1]

    if room_type == "Entire home":
        room = [1,0,0,0]
    elif room_type == "Hotel room":
        room = [0,1,0,0]
    elif room_type == "Private room":
        room = [0,0,1,0]
    elif room_type == "Shared room":
        room = [0,0,0,1]
    
    list_1 =  [clean, host, comms, loc, inst, short, check, value, accom, bedrooms, score]

    # features = list_1.extend(encoded_burough).extend(room)
    features = list_1 + encoded_burough + room

    print(features)
    ## can use a different method based on the features we use
    # features = [float(x) for x in request.form.values()]

    final_features = [np.array(features)]

    # use results to make prediction
    prediction = model.predict(final_features)[0]

    #create feedback for the result of the model
    prediction_text = f"The predicted price for your Airbnb listing is {round(prediction,0)} dollars"

    # send the prediction
    return render_template("index.html", result = prediction_text, form_inputs = inputs)


if __name__ == '__main__':
    app.run()