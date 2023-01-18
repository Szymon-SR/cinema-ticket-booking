DROP TABLE IF EXISTS Pracownik;
DROP TABLE IF EXISTS Seans;
DROP TABLE IF EXISTS Klient;
DROP TABLE IF EXISTS Rezerwacja;
DROP TABLE IF EXISTS Film;
DROP TABLE IF EXISTS Sala;
DROP TABLE IF EXISTS Bilet;
DROP TABLE IF EXISTS Miejsce;
DROP TABLE IF EXISTS Formularz;

CREATE TABLE Pracownik (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Login varchar(30) NOT NULL UNIQUE,
    Hasło varchar(30) NOT NULL,
    Imie varchar(30) NOT NULL,
    Nazwisko varchar(30) NOT NULL,
    Status varchar(30) NOT NULL,
    Telefon varchar(12) NOT NULL,
    czyKierownik integer(1)
);

CREATE TABLE Seans (
    Id varchar(10) NOT NULL,
    Termin date NOT NULL,
    Status varchar(30) NOT NULL,
    NumerSali integer(3) NOT NULL,
    FilmId varchar(5) NOT NULL,
    PracownikId integer(3) NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY(NumerSali) REFERENCES Sala(NumerSali),
    FOREIGN KEY(FilmId) REFERENCES Film(Id),
    FOREIGN KEY(PracownikId) REFERENCES Pracownik(Id)
);

CREATE TABLE Klient (
    Email varchar(50) NOT NULL,
    Telefon varchar(12),
    Imie varchar(30),
    Nazwisko varchar(30),
    PRIMARY KEY (Email)
);

CREATE TABLE Rezerwacja (
    Numer varchar(10) NOT NULL,
    Status varchar(25) NOT NULL,
    TerminZlozenia date NOT NULL,
    TerminWaznosci date NOT NULL,
    KlientEmail varchar(50) NOT NULL,
    PracownikId integer(3) NOT NULL,
    PRIMARY KEY (Numer),
    FOREIGN KEY(KlientEmail) REFERENCES Klient(Email),
    FOREIGN KEY(PracownikId) REFERENCES Pracownik(Id)
);

CREATE TABLE Film (
    Id varchar(5) NOT NULL,
    Tytul varchar(100) NOT NULL,
    CzasTrwania time,
    Gatunek varchar(30),
    OgraniczeniaWiekowe varchar(30),
    PracownikId integer(3) NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY(PracownikId) REFERENCES Pracownik(Id)
);

CREATE TABLE Sala (
    NumerSali INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Liczbakolumn integer(5) NOT NULL,
    LiczbaRzedow integer(5) NOT NULL
);

CREATE TABLE Bilet (
    Id varchar(25) NOT NULL,
    Cena numeric(19, 0) NOT NULL,
    Typ varchar(30) NOT NULL,
    IdMiejsca varchar(10) NOT NULL,
    SeansId varchar(10) NOT NULL,
    MiejsceRzad integer(3) NOT NULL,
    MiejsceKolumna integer(3) NOT NULL,
    RezerwacjaNumer varchar(10) NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY(SeansId) REFERENCES Seans(Id),
    FOREIGN KEY(MiejsceRzad, MiejsceKolumna) REFERENCES Miejsce(Rzad, Kolumna),
    FOREIGN KEY(RezerwacjaNumer) REFERENCES Rezerwacja(Numer)
);

CREATE TABLE Miejsce (
    Rzad integer(3) NOT NULL,
    Kolumna integer(3) NOT NULL,
    CzyZajete integer(1) NOT NULL,
    NumerSali integer(3) NOT NULL,
    SeansId varchar(10) NOT NULL,
    PRIMARY KEY (Rzad, Kolumna),
    FOREIGN KEY(NumerSali) REFERENCES Sala(NumerSali),
    FOREIGN KEY(SeansId) REFERENCES Seans(Id)
);

CREATE TABLE Formularz (
    Id varchar(25) NOT NULL UNIQUE,
    Tresc varchar(1000) NOT NULL,
    TerminPrzeslania date NOT NULL,
    TerminOdpowiedzi date,
    Odpowiedz varchar(1000),
    KlientEmail varchar(50) NOT NULL,
    PracownikId integer(3) NOT NULL,
    FOREIGN KEY(KlientEmail) REFERENCES Klient(Email),
    FOREIGN KEY(PracownikId) REFERENCES Pracownik(Id)
);