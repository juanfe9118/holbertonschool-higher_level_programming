#!/usr/bin/python3
"""Lists all the states"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    db = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,)
    res = db.execute('SELECT id, name FROM states ORDER BY id ASC;')
    for item in res:
        print('{}: {}'.format(item[0], item[1]))
