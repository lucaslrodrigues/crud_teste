from src.service.pessoa_service import PessoaService
from fastapi import APIRouter
from sqlalchemy.orm import Session
from typing import List
# import src.db.dependencies
from src.sql.database import SessionLocal

router = APIRouter()

class dbSession:
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

@router.get("/users", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    response = PessoaService().get_users(db=db, skip=skip, limit=limit)
    return response