#!/usr/bin/python3


""" This python file prints the name of states in hbtn_0e_0_usa database """


import MySQLdb
import sys


HOST = "localhost"


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
    query = "SELECT cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC"
    cur.execute(query, (sys.argv[4],))

    result = cur.fetchall()
    for states in result[:-1]:
        print("%s, " % states, end='')
    print("%s" % result[-1])

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
