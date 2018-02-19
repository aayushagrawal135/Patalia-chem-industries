from tkinter import *
import psycopg2 as db
fields = 'Last Name', 'First Name', 'Job', 'Country'


conn = db.connect(database="PCI", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
print("Connected to database")

def insert_tuple(entries):
    cur = conn.cursor()
    print(type(entries),len(entries))
    print(entries)
    cur.execute("INSERT INTO public.test VALUES (%s,%s,%s,%s)",(entries[0],entries[1],entries[2],entries[3]))
    conn.commit()
    print ("Operation done successfully")
    return

def fetch(entries):
    insert_entries = []
    for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text))
      insert_entries.append(text)
    insert_tuple(insert_entries)

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   b1 = Button(root, text='Insert',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   # b2 = Button(root, text='Quit', command=root.quit)
   # b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
   conn.close()
