from fastapi import FastAPI
import uvicorn
import pickle
import numpy as np
import pandas as pd

from fastapi.encoders import jsonable_encoder
from loguru import logger
from schemas.predict import MultipleBCancerDataInputs
from schemas.predict import PredictionResults

# load the model from disk
filename = filename = './model/bcancer_model_v1.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

app = FastAPI(debug=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict",response_model=PredictionResults, status_code=200)
async def predict(input_data: MultipleBCancerDataInputs) -> any:
    """
    Breast cancer prediction with random forst essemble model
    """
    logger.info(f"Making prediction on inputs: {input_data.inputs}")
    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    logger.info(f"Making prediction on inputs: {input_data}")
    result = loaded_model.predict(input_df.replace({np.nan: None}))

    results = {
            "predictions": [pred for pred in result],  # type: ignore
            "version": 'test'
        }
    logger.info(f"Prediction results: {results}")
    return results



if __name__ == '__main__':
    uvicorn.run(app)