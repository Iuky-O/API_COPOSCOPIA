from pydantic import BaseModel

class ImageBase64(BaseModel):
    image: str

class PredictionResult(BaseModel):
    prediction_en: str
    prediction_pt: str
