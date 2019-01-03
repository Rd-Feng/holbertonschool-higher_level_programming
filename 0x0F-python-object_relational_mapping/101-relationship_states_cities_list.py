#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        )
    )
    session = sessionmaker(bind=engine)()
    states = session.query(State).order_by(State.id)
    for s in states:
        print("{}: {}".format(s.id, s.name))
        for c in s.cities:
            print("\t{}: {}".format(c.id, c.name))
