from sqlalchemy.orm import Session
from typing import Optional, Union, Tuple
from backend.models.advocate import Advocate
from backend.models.client import Client
from backend.models.__init__ import get_session
from backend.utils.logger import setup_logger

logger = setup_logger('auth_crud')

def login_user(user_id: str, phone: str) -> Tuple[Optional[Union[Advocate, Client]], Optional[str]]:
    """
    Blueprint:
    1. Identify table based on ID prefix.
    2. Query DB for the user_id.
    3. Verify that the phone_number in the DB matches the input.
    """
    with get_session() as session:
        if user_id.startswith('Cl'): 
           user = session.query(Client).filter_by(client_id=user_id).first()
        else: 
           user = session.query(Advocate).filter_by(advocate_id=user_id).first()
    
    #checking if the user record exists
    if not user :
        logger.warning(f'No user with id:{user_id} found in database')
        return None, 'No user with this id exists in the database.'
    
    if user.phone_number != phone: #type: ignore
        return None, 'Invalid ID or phone number'

    return user, None