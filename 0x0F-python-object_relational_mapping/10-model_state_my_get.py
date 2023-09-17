#!/usr/bin/python3
"""
This script prints the State object.

with the name passed as argument.
"""
from sqlalchemy import create_engine
from model_state import State
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
    state_name = argv[4]
    res = session.query(State).filter(State.name.like(state_name)).first()
    if res:
        print("{}".format(res.id))
    else:
        print("Not found")
    session.close()
