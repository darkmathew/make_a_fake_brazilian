
from os.path import ( 
    abspath, 
    dirname, 
    join as path_join
)

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column, 
    ForeignKey, 
    Integer, 
    String, 
    create_engine
)

basedir = abspath(dirname(__file__))
db_file = path_join(basedir, 'database', 'address.db')

engine = create_engine(f'sqlite:///{db_file}', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Cities(Base):

    __tablename__ = 'Cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)
    state_id = Column(Integer, ForeignKey('States.id'), nullable=False)


class States(Base):
    __tablename__ = 'States'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    short_name = Column(String(5), nullable=False)


class CEPS(Base):
    __tablename__ = 'CEPS'

    id = Column(Integer, primary_key=True)
    cep = Column(String(30), nullable=True)
    logradouro = Column(String(500), nullable=False)
    nome_do_bairro = Column(String(500), nullable=False)
    city_id = Column(Integer, ForeignKey('Cities.id'), nullable=False)
    state_id = Column(Integer, ForeignKey('States.id'), nullable=False)
