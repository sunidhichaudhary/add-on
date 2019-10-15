from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///mydata.db', echo=True)
Base = declarative_base()


class Buildings(Base):
    __tablename__ = "buildings"

    buildingName = Column(String, primary_key=True)
    address = Column(String)
    l1 = Column(String)
    l2 = Column(String)
    l3 = Column(String)

    def __repr__(self):
        return "<Buildings: {}>".format(self.name)


class Room(Base):
    """"""
    __tablename__ = "rooms"

    flatno = Column(Integer, primary_key=True)
    rent = Column(Integer)
    area = Column(Integer)
    electricity = Column(String)
    maintain = Column(String)


   

# create tables
Base.metadata.create_all(engine)
