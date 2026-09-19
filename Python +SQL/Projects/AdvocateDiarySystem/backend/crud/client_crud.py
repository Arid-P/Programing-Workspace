from sqlalchemy.exc import IntegrityError
from typing import Dict, Any, Tuple, Optional
from datetime import datetime
from backend.models.client import Client
from backend.models.__init__ import get_session
from backend.utils.validators import generate_user_id
from backend.utils.logger import setup_logger

logger = setup_logger('client_crud')

def register_client(data: Dict[str, Any]) -> Tuple[Optional[str], Optional[str]]:
    """
    Blueprint:
    - data keys: 'name', 'phone'
    - Returns: (new_id, error_message)
    """
    logger.info(f"Attempting to register client with phone: {data.get('phone')}")
    
    # 1. Generate ID (Logic: user_type='client')
    uid: str = generate_user_id('client', data['phone'])
    
    # 2. Open Session and check existence
    with get_session() as session:
        client_exits = session.query(Client).filter_by(client_id=uid).first()
    if client_exits:
        return uid, "Client already registered"

    with get_session() as session: 
        try:
            new_client = Client(
                client_id=uid,
                name=data['name'],
                phone_number=data['phone'],
                created_at=datetime.strptime(
                    datetime.now().strftime('%H:%M:%S, %d %B %Y'), 
                    '%H:%M:%S, %d %B %Y'
                    )
            )
            
            session.add(new_client)
            session.commit()
            
            logger.info(f"Client {uid} successfully registered") 
            
        except IntegrityError as e:
            session.rollback()
            logger.error(f"Failed to register client: {str(e)}")
            return None, str(e)
    
    return uid, None