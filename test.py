import psycopg2 as db
import time

conn = db.connect(database="PCI", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
print("Connected to database")

cur = conn.cursor()

entries = ['asdca','bervwce','verv','vwewac']
# cur.execute("SELECT * from public.test")
cur.execute("INSERT INTO public.test VALUES (%s,%s,%s,%s)",(entries[0],entries[1],entries[2],entries[3]))

# rows = cur.fetchall()
# for row in rows:
#    print("ID = ", row[0])
#    print("NAME = ", row[1])
#    print("ID = ", row[2])
#    print("NAME = ", row[3])

conn.commit()
print ("Operation done successfully")
conn.close()
time.sl
sleep(2)
print('Exiting..')
