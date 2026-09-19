# client.py
"""
Client table definition
"""


from sqlalchemy import Column, String, DateTime, CheckConstraint
from .__init__ import Base


class Client(Base):
    __tablename__ = "clients"

    client_id = Column(String(20), primary_key=True)
    name = Column(String(100), nullable=False)
    phone_number = Column(String(10), nullable=False)
    created_at = Column(DateTime, nullable=False)

    __table_args__ = (
        CheckConstraint(
            "phone_number GLOB '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'",
            name="check_phone_10_digits"
        ),
    )
