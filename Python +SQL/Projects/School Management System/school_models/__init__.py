import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from .tables import Base, Students, Teachers 

# --- DYNAMIC PATH FIX ---
# This gets the directory where this __init__.py is (school_models/)
# then goes up one level to the project root to find/create school.db
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "school.db")

engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)
# -------------------------

# session factory
Session = scoped_session(sessionmaker(bind=engine))

Base.metadata.create_all(bind=engine)

def get_session():
    return Session()
