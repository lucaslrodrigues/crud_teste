from src.sql.database import SessionLocal

class dbSession:
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()