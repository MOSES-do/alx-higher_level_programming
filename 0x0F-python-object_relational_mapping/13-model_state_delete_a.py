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

    state = session.query(State) \
        .where(State.name.contains("a")).all()
    for name in state:
        session.delete(name)
    session.commit()
    session.close()
