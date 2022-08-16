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

model = load(open('./Models/_________________.joblib'))

#create route that renders index template
@app.route('/')
def main():

    ### Inputs via the model maybe?




    prediction_text = ""

    return render_template('index.html', result = prediction_text)

@app.route("/send", methods=["POST"])
def send():

    ## obtain form inputs from the dataframe for running the model
    # object of model = request.form["name_of_feature"]
    # object of model = request.form["name_of_feature"]
    # object of model = request.form["name_of_feature"]
    # object of model = request.form["name_of_feature"]
    # object of model = request.form["name_of_feature"]

    ## can use a different method based on the features we use
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]

    # use results to make prediction
    prediction = model.predict(final_features)[0]

    #create feedback for the result of the model
    prediction_text = f"The predicted price for your Airbnb listing is {round(prediction,0)} dollars"

    # send the prediction
    return render_template("index.html", result = prediction_text)


if __name__ == '__main__':
    app.run()