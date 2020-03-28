#!/usr/bin/python3
'''Cities listing by state module'''
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3])
    st = db.cursor()
    st.execute("SELECT cities.name FROM cities\
               LEFT JOIN states ON cities.state_id = states.id\
               WHERE states.name LIKE %s ORDER BY cities.id;", [argv[4]])
    res = st.fetchall()
    stn = ", "
    lst = []
    for i in res:
        lst.append(i[0])
    stn = stn.join(lst)
    print(stn)
    st.close()
    db.close()
