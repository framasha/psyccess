#! /usr/bin/env python
# encoding=utf8 

from sqlalchemy import create_engine, Column, String, Integer, Date, ForeignKey, select, or_, and_, asc, desc, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

engine = create_engine('sqlite:////lib86/dev/psycess/quotes.db', echo = False, encoding='utf-8')

Session = sessionmaker(bind = engine)
session = Session()
conn = engine.connect()

class Quotes(Base):
   __tablename__ = 'quotes'
   
   id = Column(Integer, primary_key = True)
   quote = Column(String(500))

Base.metadata.create_all(engine)