# backend/models/case.py
from sqlalchemy import Column, String, DateTime, Enum, ForeignKey
from .__init__ import Base
import enum

class CaseStatus(enum.Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    DISPOSED = "disposed"

class Case(Base):
    __tablename__ = "cases"

    case_id = Column(String(20), primary_key=True)  # Global stable ID
    case_number = Column(String(50), nullable=False, unique=True) # e.g., "123/2024"
    court_name = Column(String(100), nullable=False)
    
    parties = Column(String(255)) # e.g., "State vs. Sharma"
    status = Column(String(20), default="active")
    created_at = Column(DateTime, nullable=False)