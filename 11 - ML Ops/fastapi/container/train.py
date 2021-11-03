# Importing the required Python libraries
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data/2020 telco churn data - processed.csv")
df=df.dropna()
X = df.drop("churn", axis = 1)  
Y = df['churn'] 

# Create and train RF classifier (max depth intentionally long for demo purposes)
clf = RandomForestClassifier(max_depth=10)
clf.fit(X, Y)

# Save model
pkl_filename = "../model/model.pkl"
joblib.dump(clf, pkl_filename) 