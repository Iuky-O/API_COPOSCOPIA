from api.database.connection import Base, engine

def create_tables():
    from api.models import upload_imagem_model

    print("Criando as tabelas...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas.")

if __name__ == "__main__":
    create_tables()
