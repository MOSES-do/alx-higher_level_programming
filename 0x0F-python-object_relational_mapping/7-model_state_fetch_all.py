#!/usr/bin/python3

"""Class"""


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

    all_states = session.query(State).order_by(State.id.asc()).all()
    for state in all_states:
        print(f"{state.id}: {state.name}")
    
    session.close()
