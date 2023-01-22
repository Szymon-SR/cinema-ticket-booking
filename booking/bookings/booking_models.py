# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, ForeignKeyConstraint, Integer, Numeric, String, Table, Time, \
    create_engine
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Rezerwacja(Base):
    __tablename__ = 'Rezerwacja'

    Numer = Column(String(10), primary_key=True)
    Status = Column(String(25), nullable=False)
    TerminZlozenia = Column(Date, nullable=False)
    TerminWaznosci = Column(Date, nullable=False)
    KlientEmail = Column(ForeignKey('Klient.Email'), nullable=False)
    PracownikId = Column(ForeignKey('Pracownik.Id'), nullable=False)

    Klient = relationship('Klient')
    Pracownik = relationship('Pracownik')

class Bilet(Base):
    __tablename__ = 'Bilet'
    __table_args__ = (
        ForeignKeyConstraint(['MiejsceRzad', 'MiejsceKolumna'], ['Miejsce.Rzad', 'Miejsce.Kolumna']),
    )

    Id = Column(String(25), primary_key=True)
    Cena = Column(Numeric(19, 0), nullable=False)
    Typ = Column(String(30), nullable=False)
    IdMiejsca = Column(String(10), nullable=False)
    SeansId = Column(ForeignKey('Seans.Id'), nullable=False)
    MiejsceRzad = Column(Integer, nullable=False)
    MiejsceKolumna = Column(Integer, nullable=False)
    RezerwacjaNumer = Column(ForeignKey('Rezerwacja.Numer'), nullable=False)

    Miejsce = relationship('Miejsce')
    Rezerwacja = relationship('Rezerwacja')
    Sean = relationship('Sean')


engine = create_engine("sqlite:///booking/cinema_base.db", echo=True)
Base.metadata.create_all(bind=engine)