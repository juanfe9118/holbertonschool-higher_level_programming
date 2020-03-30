#!/usr/bin/python3
"""Lists all the states"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

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
    ses.query(State).filter_by(id=2).update({State.name: "New Mexico"},
                                            synchronize_session=False)
    # Save changes
    ses.commit()
    # Close the instance of session
    ses.close()
