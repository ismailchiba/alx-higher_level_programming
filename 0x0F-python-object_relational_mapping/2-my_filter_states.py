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
    sql = "SELECT * FROM states WHERE name = '{}'\
          ORDER BY id ASC;"
    cur.execute(sql.format(state_name))
    row = cur.fetchone()
    print(row)
    cur.close()
    db.close()
