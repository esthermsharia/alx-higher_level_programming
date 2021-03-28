#!/usr/bin/python3
"""
Defines a State model.
Inherits from SQLAlchemy Base and links to the MySQL table states.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.
    __tablename__ (str): The name of the MySQL table to store States.
    id:(integer) The state's id.
    name:(string) The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
