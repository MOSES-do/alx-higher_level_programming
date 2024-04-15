#!/usr/bin/python3

""" This python file prints the name of states in hbtn_0e_0_usa database """

import sys
import MySQLdb


ui = sys.argv[4]

HOST = "localhost"


def main():
    """ Executing mysql query to get states that start
        with 'N' from database table """

    db = MySQLdb.connect(
                    host=HOST,
                    user=sys.argv[1],
                    port=3306,
                    passwd=sys.argv[2],
                    db=sys.argv[3]
                )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY states.name LIKE '{placeholder}' \
    ORDER BY states.id"
    search_term = ui
    sql_query = query.format(placeholder=search_term)
    cur.execute(sql_query)
    """query = "SELECT * FROM states WHERE '{field}' = %s \
        ORDER BY states.id ASC"
    sql_query = query.format(field=name)
    cur.execute(sql_query, (ui,))"""

    result = cur.fetchall()
    for state in result:
        print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
