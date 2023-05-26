import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
import sqlalchemy.ext.declarative
from sqlalchemy.orm import sessionmaker
import mysql.connector


Base = sqlalchemy.orm.declarative_base()

class Person(Base):
    __tablename__ = 'Persons'
    id = Column(Integer, primary_key=True)
    first_name = Column("first_name", String(250))
    last_name = Column("last_name", String(250))
    race = Column("race", String(250))
    age = Column("age", Integer)
    created_date = Column("creation_date", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, first_name, last_name, race, age):
        self.first_name = first_name
        self.last_name = last_name
        self.race = race
        self.age = age
        # self.created_date=created_date



    def __repr__(self):
        return f"({self.id}, {self.first_name}, {self.last_name},  {self.race}, {self.age}) "


# <editor-fold desc="Login details">
url = 'mysql+mysqlconnector://root:password@localhost:3317/duomenu_baze' #password changed
engine = create_engine(url, echo=True)
# </editor-fold>

connection = engine.connect()

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# person = Person("Lex", "Luthor", "Man", 23)
# session.add(person)
# session.commit()

results = session.query(Person).all()
#print(results)