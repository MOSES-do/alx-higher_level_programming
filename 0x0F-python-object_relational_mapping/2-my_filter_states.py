#!/usr/bin/python3

""" This python file prints the name of states in hbtn_0e_0_usa database """

import sys
import MySQLdb


ui = sys.argv[4]

HOST = "localhost"
user = "root"
d_base = "hbtn_0e_0_usa"


def main():
    """ Executing mysql query to get states  4&5 from database table """

    db = MySQLdb.connect(host=HOST, user=user, passwd="", db=d_base)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '%{}%' \
    ORDER BY states.id".format(ui))

    result = cur.fetchall()
    for state in result:
        print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
