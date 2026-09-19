from typing import Optional
from datetime import datetime as dt
from sqlalchemy.exc import OperationalError

from backend.utils.logger import setup_logger
from backend.models import get_session
from backend.models.assignment_adv import AdvocateCaseAssignment
from backend.models.assignment_client import ClientCaseAssignment

logger = setup_logger('assignment_crud')
 
def assign_case_to_adv (adv_id, case_id) -> tuple[bool, Optional[str]]:
    """
    Docstring for assign_case_to_adv, assigns a case to a advocate
    
    :param adv_id: Description
    :param case_id: Description
    :return: Description
    :rtype: tuple[bool, str | None]
    """
    logger.info('Request to assign a case to a advocate')

    adv_assignment = AdvocateCaseAssignment(
        case_id=case_id,
        advocate_id=adv_id,
        created_at=dt.strptime(dt.now().strftime('%H:%M:%S %d %B %Y'), '%H:%M:%S %d %B %Y')
    )

    try:
        session = get_session()
        session.add(adv_assignment)
        session.commit()
    except OperationalError as e:
        logger.error('The assignment of the case failed', str(e))
        return False, str(e)

    logger.info(f'The case has been assigned sucessfully. [case_id={case_id}, adv_id={adv_id}]')
    return True, None

def assign_case_to_client (client_id, case_id) -> tuple[bool, Optional[str]]:
    """
    Docstring for assign_case_to_client, assigns a case to a client
    
    :param adv_id: Description
    :param case_id: Description
    :return: Description
    :rtype: tuple[bool, str | None]
    """
    logger.info('Request to assign a case to a client')

    adv_assignment = ClientCaseAssignment(
        case_id=case_id,
        advocate_id=client_id,
        created_at=dt.strptime(dt.now().strftime('%H:%M:%S %d %B %Y'), '%H:%M:%S %d %B %Y')
    )

    try:
        session = get_session()
        session.add(adv_assignment)
        session.commit()
    except OperationalError as e:
        logger.error('The assignment of the case failed', str(e))
        return False, str(e)

    logger.info(f'The case has been assigned sucessfully. [case_id={case_id}, client_id={client_id}]')
    return True, None