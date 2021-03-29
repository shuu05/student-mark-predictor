from flask import Flask, render_template,request
import joblib

app = Flask(__name__)

model = joblib.load('mark_predector.pkl')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/',methods=['POST'])
def marks():
    if request.method == 'POST':
        hours = float(request.form['hours'])
        mark = str(model.predict([[hours]])[0][0])

    return render_template("index.html",your_marks=mark)


if __name__ == "__main__":
    app.run(debug=True)
