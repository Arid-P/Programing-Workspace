# backend/models/__init__.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from sqlalchemy.exc import OperationalError
from config import MAIN_DB_PATH, SQLITE_ECHO

from backend.utils.logger import setup_logger
logger = setup_logger('models_init')

Base = declarative_base()

# Single engine for the unified diary database
engine = create_engine(f"sqlite:///{MAIN_DB_PATH}", echo=SQLITE_ECHO)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    # This will now create all 6 tables in one file
    try:
        import backend.models.advocate
        import backend.models.client
        import backend.models.case
        import backend.models.hearing
        import backend.models.assignment_client
        import backend.models.assignment_adv
        import backend.models.audit
        Base.metadata.create_all(engine)
    except OperationalError :
        logger.error('Table could not be initalised.', exc_info=True)
        return False
    
    logger.info('Tables have been initialised.')
    return True



def get_session():
    Session = scoped_session(SessionLocal)
    return Session()