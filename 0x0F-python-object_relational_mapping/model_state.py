#!/usr/bin/python3
"""Class representing existing table in database"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    """Class repersents structure of table"""
    __tablename__ = 'states'

    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement=True,
            unique=True
        )
    name = Column(String(128), nullable=False)
