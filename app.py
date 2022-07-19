from fastapi import FastAPI, File, UploadFile
from Model import AmostraEntenty
from Controller import TreinadorController
from pydantic import BaseModel
from typing import Union


app = FastAPI()


@app.get("/")
async def root():
    return {"PERCEPTRON": "Bem vindo ao algortimo perceptron"}


@app.post('/treinar/')
def upload_file_and_read(dataset: AmostraEntenty.Dataset, x1: Union[float, None], x2: Union[float, None], x3: Union[float, None]):
    algoritmo = TreinadorController.treinar(dataset.conteudo)
    print(algoritmo)
    x1 = x1 if 255 > x1 > 0 else 255 if x1 > 255 else 0
    x2 = x2 if 255 > x2 > 0 else 255 if x2 > 255 else 0
    x3 = x3 if 255 > x3 > 0 else 255 if x3 > 255 else 0
    cor = [x1, x2, x3]
    return {TreinadorController.calcular(algoritmo, cor)}

