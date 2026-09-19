# backend/utils/validators.py

from typing import Literal, Optional
from .logger import setup_logger
from backend.models.__init__ import get_session
from backend.models.case import Case
from backend.models.assignment_adv import AdvocateCaseAssignment

logger = setup_logger('validator')

#Some custom errors that will come in hand in future
class EmptyValueError(Exception):
    """Raised when input is empty."""
    pass

class InvalidCharacterError(Exception):
    """Raised when input contains invalid characters."""
    pass

class ValueOutOfRangeError(Exception):
    """Raised when input is outside allowed range."""
    pass


def generate_user_id (user_type: str, phone: str, role: Optional[str] = None) -> str:
    """
    Scaffold:
    - user_type: 'client' or 'advocate'
    - phone: 10-digit string
    - role: 'senior', 'junior', or None
    """
    prefix: str = ''

    if user_type == 'client':
        prefix = 'Cl'
    else:
        prefix = 'SAdv' if role == 'senior' else 'JAdv'

    logger.info(f'id has been generated, id={prefix}_{phone}')
    return f"{prefix}_{phone}"

def generate_case_id (data):
    
    #case no '3242/23' combine this case number with the court name, and a 3 letter hash, like 'CAS_3242/23_2W3_Family_Court' where 2W3 is the hash. The court name will be a optional field when we are looking (search, select query) for the case and if there are more that 1 case with this this much case id, we will ask for the court name


    ...

def validate_phone (phone: str) -> bool:
    """Check if phone is exactly 10 digits and numeric."""

    try:
        if len(phone) != 10:
            raise ValueOutOfRangeError
        phone_num = int(phone)
    except ValueError:
        logger.warning(f'The phone number provided has characters other than numbers, phone={phone}')
        return False
    except ValueOutOfRangeError:
        logger.warning(f'The phone number provided does not have 10 digits, phone={phone}')
        return False

    return True

def verify_case_assign_existence (data: dict[str, str]) -> tuple[bool, Optional[str]]:
    logger.info('Verification of case and its assignment to the advocate.')

    case_id = data['case_id']
    role = data['role']
    
    with get_session() as session:
        case_ = session.query(Case).filter_by(case_id=case_id).first()
        
    if not case_:
        logger.warning(f'The case with the id provided does not exist, case_id:{case_id}')
        return False, 'No case with such id exists'

    with get_session() as session:
        if role == 'adv':
            adv_assigned = session.query(AdvocateCaseAssignment).filter_by(advocate_id=data['adv_id']).first()
            uid =data['adv_id']
        else:
            client_assigned = session.query(AdvocateCaseAssignment).filter_by(advocate_id=data['client_id']).first()
            uid =data['client_id']
            
    if adv_assigned or client_assigned:
        logger.warning(f'The case has already been assigned case_id:{case_id}, uid:{uid}')
        return False, 'The case has adready been assigned'
    
    return True, None