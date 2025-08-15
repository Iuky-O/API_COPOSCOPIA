import os
import gdown
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODELO_NAME")
MODEL_URL = os.getenv("MODELO_URL_2")

def download_model():
    if not MODEL_NAME or not MODEL_URL:
        raise ValueError("Variáveis MODELO_NAME e MODELO_URL não configuradas no .env")

    if not os.path.exists(MODEL_NAME):
        print(f"Baixando o modelo '{MODEL_NAME}' do Google Drive...")
        gdown.download(MODEL_URL, MODEL_NAME, quiet=False)
        print("Modelo baixado com sucesso.")

        