#!/usr/bin/python3
"""Lists all the states"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(db)
    # Create a premade "Session" class
    Session = sessionmaker(bind=db)
    # Instance of the Session
    ses = Session()
    n_state = State(name="Louisiana")
    ses.add(n_state)
    ses.commit()
    # Make a query
    res = ses.query(State).filter_by(name="Louisiana").first()
    print(res.id)
    # Close the instance of session
    ses.close()
