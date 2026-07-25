# Customer Churn Predictor 

## Project Overview
This project is a full-stack Machine Learning web application. 
It acts as an early warning system for businesses. 

By analyzing basic customer behavior, the application predicts 
whether a user is likely to cancel their service (also known as "churn").

## How It Works
1. **Data Entry:** A user inputs customer metrics into a web form. 
   (e.g., how long they have been subscribed, how many support tickets they raised).
2. **Analysis:** The backend sends this data to a trained Machine Learning model.
3. **Prediction:** The model compares the data against past trends.
4. **Result:** The web interface instantly displays a "Risk Score." 

## The Business Value
Customer retention is a massive revenue driver for any company. 
It costs much more to acquire a new customer than to keep an existing one. 

I built this project to bridge the gap between raw code and management strategy. 
It turns complex data into a simple metric that business leaders can act on.

## Technologies Used
* **Machine Learning:** Python, Scikit-Learn (Random Forest), NumPy
* **Backend:** Flask (API routing and model integration)
* **Frontend:** HTML & CSS (Responsive user interface)

## How to Run It Locally

**Step 1:** Activate your Python virtual environment.
**Step 2:** Install the required libraries:
`pip install numpy scikit-learn flask`

**Step 3:** Train the model by running:
`python model.py`

**Step 4:** Start the local web server by running:
`python app.py`

**Step 5:** Open your web browser and navigate to:
`http://127.0.0.1:5000`
