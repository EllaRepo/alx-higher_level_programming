#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa
"""

import sys
from relationship_city import City
from relationship_state import Base, State
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

    # create the State "California" with the City "San Francisco"
    newState = State(name="California")
    newCity = City(name="San Francisco")
    newState.cities.append(newCity)

    session.add(newState)
    session.add(newCity)
    session.commit()

    # Close session
    session.close()
