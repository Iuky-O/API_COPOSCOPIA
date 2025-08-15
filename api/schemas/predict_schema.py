from pydantic import BaseModel
from typing import Optional, Literal

class ImageBase64(BaseModel):
    image: str
    # true_label: Optional[str] = None

class PredictionResult(BaseModel):
    prediction_en: str
    prediction_pt: str
    confidence: float
    
#     recall: Optional[float] = None

# class RecallRequest(BaseModel):
#     predicted_label: Literal["CIN1", "CIN2", "CIN3"]
#     true_label: Literal["CIN1", "CIN2", "CIN3"]
