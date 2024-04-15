#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

"""Class representing existing table in database"""


DATABASE_URL = 'mysql+mysqlconnector://root:root@localhost/hbtn_0e_6_usa'

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
