#!/usr/bin/python3
"""
this module lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')

    session.add(new_state)
    session.commit()

    target = new_state
    state = session.query(State).filter(State.name.like('Louisiana%')).order_by(State.id).all()
    if state:
        for i in state:
            print(i.id)
    else:
        print('Not found')

    session.close()
