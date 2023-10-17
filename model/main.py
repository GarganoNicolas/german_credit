from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


import pickle
import pandas as pd
from fastapi.encoders import jsonable_encoder

app = FastAPI()

with open("german_credit/model/model1.pkl", "rb") as f:
    model = pickle.load(f)

with open("german_credit/model/model1.pkl", "rb") as f:
    model = pickle.load(f)


COLUMNS_PATH = "german_credit/model/columns.pickle"
with open(COLUMNS_PATH, 'rb') as handle:
    ohe_tr = pickle.load(handle)





    
class Answer(BaseModel):
    Age                 : int
    Sex                 : str
    Job                 : str
    Housing             : str
    Saving_accounts     : str
    Checking_account    : str
    Credit_amount       : int
    Duration            : int
    Purpose             : str
  


@app.get("/")
async def root():
    return {"message": "Proyecto CREDIT  - Nicolas Gargano"}


@app.post("/prediction")
def predict(answer: Answer):

    answer_dict = jsonable_encoder(answer)
    
    for key, value in answer_dict.items():
        answer_dict[key] = [value]

    # Crear dataframe
    single_instance = pd.DataFrame.from_dict(answer_dict)


    data1 = single_instance.replace({
        'Job': {
            'unskilled and non-resident': 0, 
            'unskilled and resident': 1, 
            'skilled': 2, 
            'highly skilled': 3
        },
        'Checking_account': {
            'little': 1, 
            'moderate': 2, 
            'other': 0, 
            'rich': 3
        },
        'Saving_accounts': {
            'other': 0, 
            'little': 1, 
            'quite rich': 3, 
            'rich': 4, 
            'moderate': 2
        },
        'Sex': {
            'male': 0, 
            'female': 1
        },
        'Housing': {
            'own': 2, 
            'free': 1, 
            'rent': 0
        },

    })
    data_ohe = pd.get_dummies(data1).reindex(columns = ohe_tr).fillna(0)

    
    prediction = model.predict(data_ohe)


    # Cast numpy.int64 to just a int
    credit = int(prediction[0])


    # Adaptación respuesta
    response = credit
    if credit == 1:
        response = "Oh, we are so sorry, just today we can't give credits"
    if credit == 0:
        response = "Mister, came over here please, of course we have the MONEY you need "


    return response


# Definir en uvicorn el puerto **7860** y host **0.0.0.0**
if __name__ == '__main__':

    # 0.0.0.0 o 127.0.0.1
    uvicorn.run(app, host='0.0.0.0', port=7860)
