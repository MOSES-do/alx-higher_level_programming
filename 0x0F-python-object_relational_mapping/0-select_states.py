#!/usr/bin/python3

""" This python fie prints the name of states in hbtn_0e_0_usa database """


import MySQLdb


HOST = "localhost"
user = "root"
d_base = "hbtn_0e_0_usa"


def main():
    """ Executing mysql query to get name of states from database table """

    db = MySQLdb.connect(host=HOST, user=user, passwd="", db=d_base)
    cur = db.cursor()
    cur.execute("SELECT name FROM states ORDER BY states.id ASC")
    result = cur.fetchall()

    num = 0
    for states in result:
        num += 1
        state = "%s," % states
        new_state = state.replace(',', '')
        print(f"({num}, '{new_state}')")
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
