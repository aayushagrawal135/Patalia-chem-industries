import datetime
import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_declarative import Client, Product, Invoice, Base
from functions import *

def main():
    engine = create_engine('sqlite:///reminderSystem.db')
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    newClient = {}
    newClient['GST_no'] = 'ASdas1'
    newClient['authority_designation'] = 'manager'
    newClient['name'] = 'John Doe'
    newClient['address'] = 'abc, xyz, near lmnop'
    newClient['phoneNumber'] = '+91312312234523'

    insertClient(session, newClient)

    newClient2 = {}
    newClient2['GST_no'] = 'ASdas1234'
    newClient2['authority_designation'] = 'general manager'
    newClient2['name'] = 'John Doe'
    newClient2['address'] = 'abc, xyz, near lmnop'
    newClient2['phoneNumber'] = '+91312312234523'

    insertClient(session, newClient2)

    listAllClients(session)

if __name__ == '__main__':
    main()
