from sqlalchemy.orm import Session
import src.sql.schemas
from src.sql.models import Product, User, Wallet, Sale

class UserCrud:
    def get_users(self, db: Session, skip: int, limit: int):
        return db.query(User).offset(skip).limit(limit).all()