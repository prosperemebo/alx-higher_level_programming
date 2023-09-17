#!/usr/bin/python3
"""This script changes the name of a State object from a database."""
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
    query = session.query(State).filter(State.id == 2).first()
    query.name = "New Mexico"
    session.commit()
    session.close()
