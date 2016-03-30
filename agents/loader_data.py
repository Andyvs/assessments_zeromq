# This programs is for Loading the data in the session with the sqlite db.

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os, datetime

# the declarative_base() callable returns a new base class from which all mapped classes should inherit
Base = declarative_base()


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
    
    def __repr__(self):
        return "<MemberDetails(MEMBER_ID='%s', FIRST_NAME='%s', LAST_NAME='%s', DOB='%s', ADDRESS='%s', CITY='%s', PHONE='%s', EMAIL='%s')>" % (
                                self.MEMBER_ID, self.FIRST_NAME, self.LAST_NAME, self.DOB, self.ADDRESS, self.CITY, self.PHONE, self.EMAIL)

# engine = create_engine('postgresql://andy:@andy@/ram')
engine = create_engine('sqlite:///mbrDetials.db')

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine) 

# Create a sessionmaker bound to the engine
Session = sessionmaker(bind=engine)

# Create a session
session = Session()
# help(session)

# Date Formatting
somestring = '3/1/2008'
dob = datetime.datetime.strptime(somestring, '%d/%m/%Y').date()

# Add an instance of fooditem
table_det1 = MemberDetails(MEMBER_ID=9, FIRST_NAME='Anand', LAST_NAME='VS', \
                          DOB=dob, ADDRESS='Basavangudi', CITY='Bangalore', \
                          PHONE=1231231231, EMAIL='mail@mail.com')

table_det2 = MemberDetails(MEMBER_ID=10, FIRST_NAME='Andy', LAST_NAME='VS', \
                          DOB=dob, ADDRESS='Basavangudi', CITY='Bangalore', \
                          PHONE=1231231231, EMAIL='mail@mail.com')

# Adding to session
session.add(table_det1)
session.add(table_det2)

# # Make some queries
print session.query(MemberDetails).all()

# # Committing the session
session.commit()


