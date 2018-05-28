import datetime
import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_declarative import Client, Product, Invoice

def insert(session):

    return

def insertClient(session, data):
    new = Client(GST_no = data['GST_no'], authority_designation = data['authority_designation'], name = data['name'], address = data['address'], phoneNumber = data['phoneNumber'])
    session.add(new)
    session.commit()
    return

def listAllClients(session):
    clientList = session.query(Client).all()
    counter = 1
    for client in clientList:
        print(counter,')', client.name)

    return
