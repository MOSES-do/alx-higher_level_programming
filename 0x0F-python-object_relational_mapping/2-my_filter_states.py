#!/usr/bin/python3

""" This python file prints the name of states in hbtn_0e_0_usa database """

import sys
import MySQLdb


if len(sys.argv) < 4:
    sys.exit(1)

user_input = sys.argv[4]

HOST = "localhost"
user = "root"
d_base = "hbtn_0e_0_usa"


def main():
    """ Executing mysql query to get states  4&5 from database table """

    db = MySQLdb.connect(host=HOST, user=user, passwd="", db=d_base)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '%{}%'".format(user_input))

    result = cur.fetchone()
    print(result)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
