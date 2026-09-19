import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from .tables import Base

# This code automatically finds the folder you are in
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "school.db")

# Use 4 slashes for absolute Windows paths
engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)

# Session factory
Session = scoped_session(sessionmaker(bind=engine))

# Ensure tables are created in school.db
Base.metadata.create_all(bind=engine)

def get_session():
    return Session()