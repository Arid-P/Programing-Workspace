# backend/models/hearing.py
from sqlalchemy import Column, String, Date, DateTime, ForeignKey
from .__init__ import Base


class Hearings(Base):
    __tablename__ = "hearings"

    hearing_id = Column(String(20), primary_key=True)  # Global stable ID
    case_id = Column(String(20), ForeignKey("cases.case_id"), nullable=False) 

    hearing_date = Column(Date, nullable=False)
    previous_date = Column(Date)
    next_date = Column(Date)
    
    status = Column(String(20))
    #like, client didnt come, settled, etc
    note = Column(String(500)) 
    created_at = Column(DateTime, nullable=False)