from typing import Optional

from backend.utils.logger import setup_logger
from backend.models.__init__ import init_db, SessionLocal
from backend.utils.validators import verify_case_assign_existence
from backend.crud import assignment_crud

logger = setup_logger('main')


class Assignment():
    def assign_case (self, data: dict[str, str]):
        case_id = data['case_id']
        if data['role'] == 'adv':
            success, error = assignment_crud.assign_case_to_adv(data['adv_id'], case_id)
        else:
            success, error = assignment_crud.assign_case_to_client(data['client_id'], case_id)
        
        return success, error

    def verify_and_assign_case (self, data: dict[str, str]):
        """
        Docstring for verify_and_assign_case
        
        :param adv_id: Description
        :param case_id: Description
        """
        verified, error = verify_case_assign_existence(data)
        if not verified:
            return False, error
        
        success, error = self.assign_case(data)
        logger.info('The verification and assignment of the case both were successful')
        return success, error


    def create_and_assign_new_case (self, adv_id, data) -> tuple[bool, Optional[str]]:
        
        success, error = self.assign_case(data)
        logger.info('The verification and assignment of the case both were successful')
        return success, error


def start_backend_system() -> None:
    """Initializes database and performs startup checks."""

    initialised = init_db()

    if initialised:
        print("System Readiness: OK")
        logger.info('The system has started')
    else:
        print('System Readiness: FAILED')
        logger.critical('The system can not be operated as the tables in the database hasnt been created.')
    
    #test_registration()

if __name__ == "__main__":
    start_backend_system()