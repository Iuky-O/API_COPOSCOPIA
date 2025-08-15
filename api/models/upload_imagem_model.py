from sqlalchemy import Column, Integer, ForeignKey, String
from api.database.connection import Base

class UploadExameImagem(Base):
    __tablename__ = 'uploads_imagem'

    upload_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(45), nullable=False)
    upload = Column(String(255), nullable=False)
