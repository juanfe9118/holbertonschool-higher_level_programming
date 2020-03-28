#!/usr/bin/python3
'''States filtering by input module'''
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3])
    st = db.cursor()
    command = "SELECT `id`, `name` FROM states WHERE BINARY states.name = '{}'"
    command = command.format(argv[4])
    st.execute(command)
    res = st.fetchall()
    for i in res:
        print(i)
    db.close()
