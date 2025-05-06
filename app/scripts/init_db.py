from sqlalchemy.orm import Session
from ..db.session import engine
from models import Base
from models.user import User

def init_db():
    Base.metadata.create_all(bind=engine)