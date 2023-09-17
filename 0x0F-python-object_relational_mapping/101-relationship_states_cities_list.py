#!/usr/bin/python3
"""
This script lists all State objects, and.

corresponding City objects,contained in a databas
"""
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
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
    query = session.query(State).outerjoin(City)\
        .order_by(State.id, City.id).all()
    for states in query:
        print(f"{states.id}: {states.name}")
        for city in states.cities:
            print(f"    {city.id}: {city.name}")
    session.close()
