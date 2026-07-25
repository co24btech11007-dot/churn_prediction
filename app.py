from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open('churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    features = np.array([data])
    
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    
    result = "High Risk of Churn" if prediction == 1 else "Low Risk of Churn"
    prob_score = round(probability * 100, 2)
    
    return render_template('index.html', result=result, prob=prob_score)

if __name__ == "__main__":
    app.run(debug=True)