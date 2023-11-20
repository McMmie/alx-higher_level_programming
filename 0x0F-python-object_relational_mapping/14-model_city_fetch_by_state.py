#!/usr/bin/python3
"""
this module lists all City  objects from the database hbtn_0e_14_usa
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State, City).join(City).filter(State.id == City.state_id).order_by(City.id).all()
    for state, city in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
