#!/usr/bin/python3
"""
Script that lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create engine to connect to MySQL database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create session to interact with database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects that contain the letter a and sort them by id
    # in ascending order
    states = session.query(State.name.like('%a%')).order_by(State.id).all()

    # Print each State object in the format "{id}: {name}"
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
