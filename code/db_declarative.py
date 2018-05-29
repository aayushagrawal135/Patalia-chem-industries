from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Float

Base = declarative_base()

class Client(Base):
    __tablename__ = 'client'
    GST_no = Column(String(15), primary_key=True)
    authority_designation = Column(String(20), nullable=False)
    name = Column(String(50), nullable=False)
    address = Column(String(200), nullable=False)
    phoneNumber = Column(String(15))

class Product(Base):
    __tablename__ = 'product'
    HSN_code = Column(String(12), primary_key=True)
    product_name = Column(String(30), nullable=False)

class Orders(Base):
    __tablename__ = 'orders'
    PO_no = Column(String(50), primary_key=True)
    GST_no = Column(String(15), ForeignKey('client.GST_no', ondelete='CASCADE', onupdate='CASCADE'))
    freight = Column(Integer)
    no_of_packages = Column(String(30))
    order_description = Column(String(200))
    quantity = Column(Integer)
    quantity_unit = Column(String(20))
    rate = Column(Float(6,2))
    tax = Column(Float(4,2))
    delivery_address = Column(String(200))
    packing_charges = Column(Integer)

class Invoice(Base):
    __tablename__ = 'invoice'
    invoice_no = Column(String(10), primary_key=True)
    invoice_date = Column(DateTime)
    PO_no = Column(String(50), ForeignKey('orders.PO_no', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    LR_no = Column(String(12))
    LR_date = Column(DateTime)
    amount = Column(Float(10,0))

class Enquiry(Base):
    __tablename__ = 'enquiry'
    enquiry_no = Column(String(50), primary_key=True)
    GST_no = Column(String(15), ForeignKey('client.GST_no'))
    enquiry_date = Column(DateTime)
    HSN_code = Column(String(12))
    product_quantity = Column(Integer)
    our_offer_no = Column(String(50))
    our_offer_date = Column(DateTime)
    ex_works_rate = Column(Float(6,2))
    for_destination_rates = Column(Float(6,2))
    transport_charges = Column(Float(6,2))
    payment_terms = Column(String(200))

engine = create_engine('sqlite:///pci.db')
Base.metadata.create_all(engine)
