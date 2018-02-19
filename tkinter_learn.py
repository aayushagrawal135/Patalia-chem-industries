import tkinter as tk
from tkinter import *
from tkinter import ttk
import psycopg2 as db

fields = 'First Name', 'Last Name', 'Job', 'Country'

LARGE_FONT= ("Verdana", 12)


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Insert entry",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Delete entry",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()



class PageOne(tk.Frame) :

    def __init__(self, parent, controller):

        self.conn = db.connect(database="PCI", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        print("Connected to database")

        Frame.__init__(self, parent)
        entries = []
        i=0

        for field in fields:
            Label(self, text=field).grid(row=i, column=0, sticky=W)
            fname = Entry(self)
            fname.grid(row=i, column=1, sticky=W)
            entries.append((field,fname))
            i+=1

        b1 = Button(self, text='Insert', command=(lambda e=entries: self.fetch(e)))
        b1.grid(row=i, column=0, sticky=W)

        button2 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button2.grid(row=i, column=1, sticky=W)


    def fetch(self,entries):
        insert_entries = []
        for entry in entries:
          field = entry[0]
          text  = entry[1].get()
          print('%s: "%s"' % (field, text))
          insert_entries.append(text)
        self.insert_tuple(insert_entries)

    def insert_tuple(self,entries):
        cur = self.conn.cursor()
        print(type(entries),len(entries))
        print(entries)
        cur.execute("INSERT INTO public.test VALUES (%s,%s,%s,%s)",(entries[0],entries[1],entries[2],entries[3]))
        self.conn.commit()
        print ("Operation done successfully")
        return

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()



app = App()
app.mainloop()
