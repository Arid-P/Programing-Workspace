# backend/models/assignment_client.py
from sqlalchemy import Column, String, DateTime, ForeignKey
from . import Base


class ClientCaseAssignment(Base):
    __tablename__ = "assignments_client"

    assign_client_id = Column(String(20), primary_key=True)  # Global stable ID

    case_id = Column(String(20), ForeignKey("cases.case_id"), nullable=False) 
    client_id = Column(String(20), ForeignKey("clients.client_id"), nullable=False)
    
    created_at = Column(DateTime, nullable=False)

