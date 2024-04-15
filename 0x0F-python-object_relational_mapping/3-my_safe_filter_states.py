#!/usr/bin/python3

""" This python file prints the name of states in hbtn_0e_0_usa database """

import sys
import MySQLdb


user_input = sys.argv[4]

HOST = "localhost"


def main():
    """ Executing mysql query to get states
    that start with 'N' from database table """

    db = MySQLdb.connect(
                    host=HOST,
                    user=sys.argv[1],
                    port=3306,
                    passwd=sys.argv[2],
                    db=sys.argv[3]
                )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s \
    ORDER BY states.id ASC LIMIT 1"
    cur.execute(query, (user_input,))

    result = cur.fetchall()

    for state in result:
        print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
