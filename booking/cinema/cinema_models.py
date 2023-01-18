# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, ForeignKeyConstraint, Integer, Numeric, String, Table, Time
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Sala(Base):
    __tablename__ = 'Sala'

    NumerSali = Column(Integer, primary_key=True)
    Liczbakolumn = Column(Integer, nullable=False)
    LiczbaRzedow = Column(Integer, nullable=False)


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)

class Film(Base):
    __tablename__ = 'Film'

    Id = Column(String(5), primary_key=True)
    Tytul = Column(String(100), nullable=False)
    CzasTrwania = Column(Time)
    Gatunek = Column(String(30))
    OgraniczeniaWiekowe = Column(String(30))
    PracownikId = Column(ForeignKey('Pracownik.Id'), nullable=False)

    Pracownik = relationship('Pracownik')

t_Formularz = Table(
    'Formularz', metadata,
    Column('Id', String(25), nullable=False),
    Column('Tresc', String(1000), nullable=False),
    Column('TerminPrzeslania', Date, nullable=False),
    Column('TerminOdpowiedzi', Date),
    Column('Odpowiedz', String(1000)),
    Column('KlientEmail', ForeignKey('Klient.Email'), nullable=False),
    Column('PracownikId', ForeignKey('Pracownik.Id'), nullable=False)
)

class Seans(Base):
    __tablename__ = 'Seans'

    Id = Column(String(10), primary_key=True)
    Termin = Column(Date, nullable=False)
    Status = Column(String(30), nullable=False)
    NumerSali = Column(ForeignKey('Sala.NumerSali'), nullable=False)
    FilmId = Column(ForeignKey('Film.Id'), nullable=False)
    PracownikId = Column(ForeignKey('Pracownik.Id'), nullable=False)

    Film = relationship('Film')
    Sala = relationship('Sala')
    Pracownik = relationship('Pracownik')

class Miejsce(Base):
    __tablename__ = 'Miejsce'

    Rzad = Column(Integer, primary_key=True, nullable=False)
    Kolumna = Column(Integer, primary_key=True, nullable=False)
    CzyZajete = Column(Integer, nullable=False)
    NumerSali = Column(ForeignKey('Sala.NumerSali'), nullable=False)
    SeansId = Column(ForeignKey('Seans.Id'), nullable=False)

    Sala = relationship('Sala')
    Sean = relationship('Sean')