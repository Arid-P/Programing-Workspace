# backend/models/assignment_adv.py
from sqlalchemy import Column, String, DateTime, ForeignKey
from . import Base


class AdvocateCaseAssignment(Base):
    __tablename__ = "assignment_adv"

    assign_adv_id = Column(String(20), primary_key=True)  # Global stable ID

    case_id = Column(String(20), ForeignKey("cases.case_id"), nullable=False) 
    advocate_id = Column(String(20), ForeignKey("advocates.advocate_id"), nullable=False)
    
    created_at = Column(DateTime, nullable=False)

