#!/usr/bin/python3
"""Filters all the states that have 'a' in their name"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

if __name__ == "__main__":
    db = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(db)
    # Create a premade "Session" class
    Session = sessionmaker(bind=db)
    # Instance of the Session
    ses = Session()
    # Make a query
    res = ses.query(State).filter(State.name.like(func.binary('%a%')))\
        .order_by(State.id).all()
    for item in res:
        print('{}: {}'.format(item.id, item.name))
    # Close the instance of session
    ses.close()
