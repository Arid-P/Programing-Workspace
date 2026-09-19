"""
class Case(Base):
    __tablename__ = "cases"

    case_id = Column(String(20), primary_key=True)  # Global stable ID
    case_number = Column(String(50), nullable=False, unique=True) # e.g., "123/2024"
    court_name = Column(String(100), nullable=False)
    
    parties = Column(String(255)) # e.g., "State vs. Sharma"
    status = Column(String(20), default="active")
    created_at = Column(DateTime, nullable=False)
"""

from sqlalchemy.exc import IntegrityError
from typing import Any, Optional
from datetime import datetime
from backend.models.__init__ import get_session
from backend.models.case import Case
from backend.utils.validators import generate_user_id
from backend.utils.logger import setup_logger

logger = setup_logger('advocate_crud')


def add_case (data: dict[str, Any]) -> tuple[Optional[str], Optional[str]]:
    """
    Blueprint:
    - data keys: 'name', 'phone', 'role', 'senior_id'
    - Returns: (new_id, error_message)
    """
    logger.info('Adding New Record requested')
    uid = generate_user_id('advocate', data['phone'], data['role'])
    
    #Checking if the uid exists already
    with get_session() as session:
        advocate_exist = session.query(Case).filter_by(advocate_id=uid).first()
    
    if advocate_exist:
            logger.warning(f'The advocate with id:{uid} already exists. No new advocate record created')
            return uid, "The user with this id already exits" 
    
    #adding the new advocate record 
    with get_session() as session:
        try:
            new_advocate = Case(
                advocate_id=uid, 
                name=data['name'], 
                role=data['role'], 
                senior_id=data['senior_id'], 
                phone_number=data['phone'], 
                created_at=datetime.strptime(
                    datetime.now().strftime('%H:%M:%S, %d %B %Y'), 
                    '%H:%M:%S, %d %B %Y'
                    )
            )
            session.add(new_advocate)
            session.commit()
            logger.info(f'new advocate has been created, with id:{uid}')
        except IntegrityError as e:
            session.rollback()
            logger.error(f"Failed to register advocate: {str(e)}")
            return None, str(e)

    return uid, None