#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

import sys
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    newstate = State(name='Louisiana')
    session.add(newstate)
    newstate1 = session.query(State).filter(State.name == 'Louisiana').first()
    session.commit()
    print("{}".format(newstate1.id))
    session.close()
