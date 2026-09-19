# advocate.py
"""
Advocate table definition
"""

from sqlalchemy import Column, String, DateTime, CheckConstraint
from backend.models.__init__ import Base

class Advocate(Base):
    __tablename__ = "advocates"

    advocate_id = Column(String(10), primary_key=True)
    name = Column(String(50), nullable=False)
    role = Column(String(10), nullable=False)  # senior | junior
    senior_id = Column(String(10), nullable=True)

    phone_number = Column(String(10), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False)

    __table_args__ = (
        CheckConstraint(
            "phone_number GLOB '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'",
            name="check_phone_10_digits"
        ),
    )

