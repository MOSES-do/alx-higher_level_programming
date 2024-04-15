#!/usr/bin/python3

""" This python file prints the name of states in hbtn_0e_0_usa database """

import sys
import MySQLdb


HOST = "localhost"
user = "root"
d_base = "hbtn_0e_0_usa"


def main():
    """ Executing mysql query to get states  4&5 from database table """
    db = MySQLdb.connect(
                    host=HOST,
                    user=sys.argv[1],
                    port=3306,
                    passwd=sys.argv[2],
                    db=sys.argv[3]
                 )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE id = %s OR id = %s ORDER BY \
            states.id ASC", (4, 5))

    result = cur.fetchall()

    for states in result:
        print(states)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()