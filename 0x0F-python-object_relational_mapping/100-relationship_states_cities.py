#!/usr/bin/python3
"""
This script that creates the State 'California' with the City.

'San Francisco' from a database.
"""
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker

from sys import argv

if __name__ == "__main__":
    db_name = argv[3]
    db_user = argv[1]
    db_password = argv[2]
    uri = "mysql://{}:{}@\
localhost:3306/{}".format(db_user, db_password, db_name)

    engine = create_engine(uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="California")
    session.add(state)
    city = City(name="San Francisco", state=state)
    session.add(city)
    session.commit()
    session.close()
