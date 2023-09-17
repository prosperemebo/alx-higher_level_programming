#!/usr/bin/python3
"""This script that lists all City objects from a database."""
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

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
    query = session.query(City, State).join(State).all()
    for cities, states in query:
        print(f"{cities.id}: {cities.name} -> {states.name}")
    session.close()
