


-- Create the Enquiry table in the end!!!!

CREATE SCHEMA pci;
SET SEARCH_PATH to pci;
SET DateStyle TO European;

CREATE TABLE Client (
    GST_no varchar(15),
    authority_designation varchar(20),
    name varchar(50) NOT NULL,
    address varchar(100),
    PRIMARY KEY (GST_no)
);

CREATE TABLE Product (
  HSN_code decimal(12,0),
  product_name varchar(30),
  PRIMARY KEY (HSN_code)
);

CREATE TABLE Orders (
  PO_no varchar(50),
  GST_no varchar(15),
  freight decimal(8,0),
  no_of_packages varchar(30),
  order_description varchar(200),
  quantity integer,
  quantity_unit varchar(20),
  rate decimal(6,2),
  tax decimal(4,2),
  delivery_address varchar(200),
  packing_charges decimal(4,0),
  PRIMARY KEY (PO_no),
  FOREIGN KEY (GST_no) REFERENCES Client (GST_no)
  	ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Invoice (
  invoice_no varchar(10),
  invoice_date date,
  PO_no varchar(50),
  LR_no decimal(12,0),
  LR_date date,
  amount decimal(10,0),
  PRIMARY KEY (invoice_no, PO_no),
  FOREIGN KEY (PO_no) REFERENCES Orders (PO_no)
  	ON DELETE CASCADE ON UPDATE CASCADE
 );

 CREATE TABLE Enquiry(
  enquiry_no varchar(50),
  GST_no varchar(15),
  enquiry_date date,
  HSN_code decimal(12,0)
  Product quantity
  our offer no.
  our offer date
  ex-works rates
  FOR destination rates
  transport charges
  Payment terms
  comparative chart of rates of all bidders
  L1 rates
 );
