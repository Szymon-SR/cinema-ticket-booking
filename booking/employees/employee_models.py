# coding: utf-8
from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    ForeignKeyConstraint,
    Integer,
    Numeric,
    String,
    Table,
    Time,
)
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from booking import Base
from flask_login import UserMixin

# Base = declarative_base()
metadata = Base.metadata


class Pracownik(Base, UserMixin):
    __tablename__ = "Pracownik"

    Id = Column(Integer, primary_key=True)
    Login = Column(String(30), nullable=False)
    Hasło = Column(String(30), nullable=False)
    Imie = Column(String(30), nullable=False)
    Nazwisko = Column(String(30), nullable=False)
    Status = Column(String(30), nullable=False)
    Telefon = Column(String(12), nullable=False)
    czyKierownik = Column(Integer)

    def get_id(self):
        return self.Id
