from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__,static_folder="static",template_folder="template")


# Load your machine learning models
car_price_prediction_model = pickle.load(open("car_price_prediction_model.sav", "rb"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/car_price_prediction", methods=["POST"])
def predict_car_price():
    if request.method == "POST":
        # Retrieve form data
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]

        # Perform prediction using the loaded model
        car_pricee = car_price_prediction_model.predict(final_features)
        car_price=round(car_pricee[0],2)
        return render_template(
            "index.html",
            car_price_prediction_text=float(car_price)
        )


if __name__ == "__main__":
    app.run(debug=True)
