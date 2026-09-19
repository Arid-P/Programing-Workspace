# backend/models/audit.py
from sqlalchemy import Column, String, DateTime, Text, ForeignKey
from .__init__ import Base

class AuditTrail(Base):
    __tablename__ = "audit_trail"

    audit_id = Column(String(20), primary_key=True)
    entity_type = Column(String(20), nullable=False) # 'case', 'hearing', 'client'
    entity_id = Column(String(20), nullable=False)
    action = Column(String(10), nullable=False)      # 'INSERT', 'UPDATE'
    
    # Physical Foreign Key to the advocates table
    changed_by = Column(String(10), ForeignKey("advocates.advocate_id"), nullable=False)
    
    timestamp = Column(DateTime, nullable=False)
    old_value = Column(Text) # JSON string
    new_value = Column(Text) # JSON string