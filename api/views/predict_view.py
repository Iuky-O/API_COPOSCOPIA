from fastapi import APIRouter, HTTPException
from http import HTTPStatus
from api.schemas.predict_schema import ImageBase64, PredictionResult
from api.controllers.predict_controller import predict_image

router = APIRouter()

@router.post("/predict", response_model=PredictionResult, status_code=HTTPStatus.OK)
async def predict(data: ImageBase64):
    try:
        result = predict_image(data.image)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/predict/ping")
async def ping():
    return {"status": "ok"}