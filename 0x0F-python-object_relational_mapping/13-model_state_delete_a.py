#!/usr/bin/python3
"""
This script that deletes all State objects.

with a name containing the letter a from a database
"""
from sqlalchemy import create_engine
from model_state import Base, State
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
    res = session.query(State).filter(State.name.ilike("%a%")).all()
    for row in res:
        session.delete(row)
    session.commit()
    session.close()
