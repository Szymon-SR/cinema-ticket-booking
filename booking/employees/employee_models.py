# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, ForeignKeyConstraint, Integer, Numeric, String, Table, Time, \
    create_engine
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Pracownik(Base):
    __tablename__ = 'Pracownik'

    Id = Column(Integer, primary_key=True)
    Login = Column(String(30), nullable=False)
    Hasło = Column(String(30), nullable=False)
    Imie = Column(String(30), nullable=False)
    Nazwisko = Column(String(30), nullable=False)
    Status = Column(String(30), nullable=False)
    Telefon = Column(String(12), nullable=False)
    czyKierownik = Column(Integer)


engine = create_engine("sqlite:///booking/cinema_base.db", echo=True)
Base.metadata.create_all(bind=engine)
