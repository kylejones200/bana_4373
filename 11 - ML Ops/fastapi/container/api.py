import pandas as pd
import joblib
from fastapi import FastAPI, Request
from pydantic import BaseModel



## API INSTANTIATION
## ----------------------------------------------------------------

# Instantiating FastAPI
api = FastAPI()

# Loading in model from serialized .pkl file
pkl_filename = "../model/model.pkl"
clf = joblib(pkl_filename)

# Creating the data model for data validation
class CLF(BaseModel):
	account_length: int	
	international_plan: int	
	voice_mail_plan: int
	number_vmail_messages: int	
	total_day_calls: int	
	total_eve_calls: int	
	number_customer_service_calls: int
	
	
## API ENDPOINTS
## ----------------------------------------------------------------

# Defining a test root path and message
@api.get('/')
def root():
	return {'message': 'Hello friends!'}
	
	
	
# Defining the prediction endpoint without data validation
@api.post('/basic_predict')
async def basic_predict(request: Request):
	
	# Getting the JSON from the body of the request
	input_data = await request.json()
	
	# Converting JSON to Pandas DataFrame
	input_df = pd.DataFrame([input_data])
	
	# Getting the prediction from the Logistic Regression model
	pred = clf.predict(input_df)[0]
	
	return pred
	
	
	
# Defining the prediction endpoint with data validation
@api.post('/predict')
async def predict(iris: CLF):
	
	# Converting input data into Pandas DataFrame
	input_df = pd.DataFrame([iris.dict()])
	
	# Getting the prediction from the Logistic Regression model
	pred = clf.predict(input_df)[0]
	
	return pred