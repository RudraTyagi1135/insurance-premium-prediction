#basic import
from fastapi import FastAPI 
from fastapi.responses import JSONResponse


#Internal Imports
from schema.user_input import UserInput
from model.prediction import MODEL_VERSION, ModelArtifactNotFoundError, predict_output
from schema.prediction_response import PredictionResponse

#fastapi object
app = FastAPI()


#home route
@app.get("/")
def home():
    return {'Message': "INSURANCE PREMIUM PREDICTION MODEL"}


#health check route {machine Readable }
@app.get("/health")
def health():
    return {
        "status" : "OK",
        "model_version" : MODEL_VERSION
    }


#prediction route
@app.post("/predict", response_model=PredictionResponse)
async def predict_premium(data: UserInput):

    user_input = {
        'bmi' : data.bmi,
        'age_group' : data.age_group,
        'lifestyle_risk' : data.lifestyle_risk,
        'city_tier' : data.city_tier,
        'income_lpa' : data.income_lpa,
        'occupation' : data.occupation
    }

    try:
        #predict result using predict_output function
        prediction = predict_output(user_input)
        
        #return result
        return prediction

    except ModelArtifactNotFoundError as e:
        return JSONResponse(status_code=503 , content=str(e))

    except Exception as e:
        return JSONResponse(status_code=500 , content=str(e))




