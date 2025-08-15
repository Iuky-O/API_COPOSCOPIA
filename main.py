from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.views import predict_view

app = FastAPI()

# CORS
app.add_middleware(
   CORSMiddleware,
   allow_origins=["*"],
   allow_methods=["*"],
   allow_headers=["*"],
)

# Rotas
app.include_router(predict_view.router, prefix="/api", tags=["Predição"])

@app.get("/")
def root():
   return {"message": "API de classificação de folhas ativa!"}
