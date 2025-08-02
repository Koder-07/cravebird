from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey,TIMESTAMP,Boolean
from sqlalchemy.sql import text

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    user_id = Column(String,  nullable=False)
    email = Column(String, unique=True, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    password = Column(String, nullable=False)
    phone_number=Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
