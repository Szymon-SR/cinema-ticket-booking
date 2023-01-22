# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, ForeignKeyConstraint, Integer, Numeric, String, Table, Time, \
    create_engine
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# metadata = Base.metadata

class Klient(Base):
    __tablename__ = 'Klient'

    Email = Column(String(50), primary_key=True)
    Telefon = Column(String(12))
    Imie = Column(String(30))
    Nazwisko = Column(String(30))


engine = create_engine("sqlite:///booking/cinema_base.db", echo=True)
Base.metadata.create_all(bind=engine)

