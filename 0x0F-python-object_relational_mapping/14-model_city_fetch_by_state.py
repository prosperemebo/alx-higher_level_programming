#!/usr/bin/python3
"""This script prints all City objects from a database."""
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

from sys import argv

if __name__ == "__main__":
    db_name = argv[3]
    db_user = argv[1]
    db_password = argv[2]
    uri = "mysql://{}:{}@\
localhost:3306/{}".format(db_user, db_password, db_name)

    engine = create_engine(uri)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City, State)\
        .join(State, State.id == City.state_id).all()
    for cities, states in query:
        print(f"{states.name}: ({cities.id}) {cities.name}")
    session.close()
