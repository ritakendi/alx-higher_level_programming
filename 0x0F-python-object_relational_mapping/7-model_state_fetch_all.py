#!/usr/bin/python3
"""lists all State objects from the database with ORM"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    # required arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password,
                                   database_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
