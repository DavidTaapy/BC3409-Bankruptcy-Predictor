# Import Libraries
from flask import Flask
from flask import request, render_template
from keras.models import load_model

# Initialise Application
app = Flask(__name__)

# Function To Get Value
def getValue(x):
    return x[0][0]

# Render The Template
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        NPTA = float(request.form.get("NPTA"))
        TLTA = float(request.form.get("TLTA"))
        WCTA = float(request.form.get("WCTA"))
        model = load_model("bankruptcy")
        prediction = model.predict([[NPTA, TLTA, WCTA]])
        value = getValue(prediction)
        result = f"The predicted value for bankruptcy is {value:.2f}!"
        return(render_template("index.html", result = result))
    else:
        return(render_template("index.html", result = "Please enter the required inputs!"))

# Run The Application
if __name__ == "__main__":
    app.run()

