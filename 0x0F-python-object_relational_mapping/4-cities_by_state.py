#!/usr/bin/python3
'''Cities listing by state module'''
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3])
    st = db.cursor()
    st.execute("SELECT cities.id, cities.name, states.name FROM cities\
               LEFT JOIN states ON cities.state_id = states.id\
               ORDER BY cities.id;")
    res = st.fetchall()
    for i in res:
        print(i)
    st.close()
    db.close()
