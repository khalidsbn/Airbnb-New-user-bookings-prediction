""" Flask app """

import pickle
import pandas as pd
from functions import feature_encoder
from flask import Flask, request, render_template

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route('/answer')
def answer():
    """
    HTML page that had the answer to the user
    """
    return render_template("answer.html")

@flask_app.route('/')
def home():
    """
    return index.html page, the main page.
    """
    return render_template("index.html")

@flask_app.route('/predict', methods=['POST'])
def predict():
    """
    Make the prediction whit new data
    """
    # Get input values from form
    input_data = request.form.to_dict()
    # Prepare input data as DataFrame
    input_df = pd.DataFrame(input_data, index=[0])

    # Processing
    encoding_cols = input_df.select_dtypes('object').columns.tolist()
    input_df = feature_encoder(input_df, encoding_cols)

    prediction = model.predict(input_df) # Prediction

    if prediction[0] == 0:
        return render_template('answer.html', prediction_text='Based on your information, you are going to make a book on AirBnB!')
    else:
        return render_template('answer.html', prediction_text='Based on your information, you are not going to make a book on AirBnB. It is best for your to delete your account so you don\'t lose your time.')


if __name__ == "__main__":
    flask_app.run(debug=True)
    