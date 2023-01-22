# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, ForeignKeyConstraint, Integer, Numeric, String, Table, Time
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_login import UserMixin




engine = create_engine('sqlite:///cinema_base.db', \
                       convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
metadata = Base.metadata


class Klient(Base):
    __tablename__ = 'Klient'

    Email = Column(String(50), primary_key=True)
    Telefon = Column(String(12))
    Imie = Column(String(30))
    Nazwisko = Column(String(30))


class Pracownik(Base, UserMixin):
    __tablename__ = 'Pracownik'

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


# class Formularz(Base):
#     __tablename__ = 'Formularz'
#
#     Id = Column(String(5), primary_key=True),
#     Tresc = Column(String(1000), nullable=False),
#     TerminPrzeslania = Column(Date, nullable=False)
#     TerminOdpowiedzi = Column(Date),
#     Odpowiedz = Column(String(1000)),
#     KlientEmail = Column(ForeignKey('Klient.Email'), nullable=False)
#     PracownikId = Column(ForeignKey('Pracownik.Id'))
#
#     klient = relationship('Klient')
#     Pracownik = relationship('Pracownik')


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


class Sean(Base):
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
