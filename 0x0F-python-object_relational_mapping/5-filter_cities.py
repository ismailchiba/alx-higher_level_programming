#!/usr/bin/python3
"""  list all existing states from hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()
    state_name = sys.argv[4]
    sql = "SELECT cities.name FROM cities JOIN states\
        ON cities.state_id = states.id WHERE \
        states.name LIKE BINARY %s\
        ORDER BY cities.id ASC;"
    cur.execute(sql, (state_name,))
    rows = cur.fetchall()
    city_names = [row[0] for row in rows]
    print(', '.join(city_names))
    cur.close()
    db.close()
