#!/usr/bin/python3

"""QUERYING OUR DATABASE TO FETCH TABLE VALUES"""


if __name__ == '__main__':
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State

    engine = create_engine(
            f"mysql+mysqldb://{argv[1]}:\
            {argv[2]}@localhost:3306/{argv[3]}"
        )

    Session = sessionmaker(bind=engine)
    session = Session()
    name = argv[4]

    state = session.query(State). \
        filter(State.name.like('%'+name+'%')).first()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
