import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

X = np.array([
    [12, 50, 10, 1],
    [2, 90, 2, 4],
    [24, 40, 20, 0],
    [1, 100, 1, 5],
    [60, 105, 50, 2]
])
y = np.array([0, 1, 0, 1, 0])

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

with open('churn_model.pkl', 'wb') as f:
    pickle.dump(model, f)