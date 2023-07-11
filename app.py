from flask import Flask, render_template,request
import pickle
import numpy as np
import pickle
import pickle
app = Flask(__name__, template_folder='templates')

model = pickle.load(open("class.pkl", "rb"))

@app.route("/")
def home():
    return  render_template("index.html")

    

@app.route("/predict", methods=["POST"])
def predict():
    # float_features = [int(x) for x in request.form.values()]
    # features = [np.array(float_features)]
    # new_data = pd.DataFrame({'store': [1], 'item': [16], 'year': [2025], 'month': [4], 'day': [1], 'weekday': [3]})

    int_features = [int(x) for x in request.form.values()]
    features = [np.array(int_features)]
    prediction = model.predict(features)

    return render_template("index.html", prediction_text = "No of Sales Predicted : {}  Initial Data Given  : {}".format(prediction, int_features))

if __name__=="__main__":
    app.run()
