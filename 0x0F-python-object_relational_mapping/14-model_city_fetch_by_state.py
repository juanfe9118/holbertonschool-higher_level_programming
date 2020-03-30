#!/usr/bin/python3
"""Lists all the states"""
from sys import argv
from model_state import Base, State
from model_city import City
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
    # Make a query
    res = ses.query(State, City).order_by(City.id).filter(State.id ==
                                                          City.state_id)
    for item in res:
        print('{}: ({}) {}'.format(item[0].name, item[1].id, item[1].name))
    # Close the instance of session
    ses.close()
