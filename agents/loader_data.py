# This programs is for Loading the data in the session with the sqlite db.

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os, datetime
import zmq
import json

# the declarative_base() callable returns a new base class from which all mapped classes should inherit
Base = declarative_base()

# engine = create_engine('postgresql://andy:@andy@/ram')
engine = create_engine('sqlite:///mbrDetials.db')

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine) 

# Create a sessionmaker bound to the engine
Session = sessionmaker(bind=engine)

class MemberDetails(Base):
    """ A declarative class for the fooditem table """
    
    __tablename__ = 'mbrdet'
    
    MEMBER_ID = Column(Integer, primary_key=True)
    FIRST_NAME = Column(String(32))
    LAST_NAME = Column(String(32))
    DOB = Column(String(32))
    ADDRESS = Column(String(32))
    CITY = Column(String(32))
    PHONE = Column(Integer)
    EMAIL = Column(String)
    


# Getting the data from Transformer which are validated and Adding to the session instant.
context = zmq.Context()
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://127.0.0.1:5558")
load_data = receiver.recv()
row_data = json.loads(load_data)

# Date Formatting
# DOB = datetime.datetime.strptime(row_data['DOB'], '%d/%m/%Y').date()

# Add an instance of fooditem
table_det1 = MemberDetails(MEMBER_ID=row_data['MEMBER_ID'], 
                          FIRST_NAME=row_data['FIRST_NAME'],
                          LAST_NAME=row_data['LAST_NAME'],
                          DOB=row_data['DOB'], 
                          ADDRESS=row_data['ADDRESS'], 
                          CITY=row_data['CITY'],
                          PHONE=row_data['PHONE'],
                          EMAIL=row_data['EMAIL'])


# Create a session
session = Session()
# help(session)

# Adding to session
session.add(table_det1)

# # Make some queries
print session.query(MemberDetails).all()

# # Committing the session
session.commit()


