#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from model_state import Base, State
from model_city import City
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

    # Query all City objects and print them in the specified format
    cities = session.query(City, State).filter(State.id == City.state_id).all()
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()
