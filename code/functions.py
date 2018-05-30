import datetime
import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_declarative import Client, Product, Invoice

def insert(session, entries):
    fields = ['GST_no','authority_designation','name','address','HSN_code','product_name','PO_no','freight','no_of_packages','order_description','quantity','quantity_unit','rate','tax','delivery_address','packing_charges','invoice_no','invoice_date','LR_no','LR_date']

    for key in entries.keys():
        print(entries[key])
    return

def insertClient(session, data):
    new = Client(GST_no = data['GST_no'], authority_designation = data['authority_designation'], name = data['name'], address = data['address'], phoneNumber = data['phoneNumber'])
    session.add(new)
    session.commit()
    return

def deleteClient(session, data):
    old = session.query(Client).filter(Client.name == data['name'], Client.authority_designation == data['authority_designation']).all()
    # print(len(old))
    for i in range(len(old)):
        session.delete(old[i])
    session.commit()
    return

def listAllClients(session):
    clientList = session.query(Client).all()
    counter = 1
    for client in clientList:
        print(counter,')', client.name, ', ', client.authority_designation)

    return
