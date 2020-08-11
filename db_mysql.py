# import MySQLclient
#
# # Open database connection
# db = MySQLdb.connect("Install_base")
#
# # prepare a cursor object using cursor() method
# cursor = db.cursor()
#
# # execute SQL query using execute() method.
# cursor.execute("SELECT * from Install_base")
#
# # Fetch a single row using fetchone() method.
# data = cursor.fetchone()
# print ("Database version : %s " % data)
#
# # disconnect from server
# db.close()


import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='mydb')
cursor = mydb.cursor()

csv_data = csv.reader(("SCU-SilfexIBbyShipTov2.csv"))
for row in csv_data:

cursor.execute (CREATE TABLE `silfexshipto` (
                   `﻿Ship Date` text,
                   `Ship To` int(11) DEFAULT NULL,
          `Region` text,
          `Serial` text,
          `Superior Serial` text,
          `System` text,
          `Material` text,
          `Quantity` int(11) DEFAULT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;)',
                  row)
        #close the connection to the database.
mydb.commit()
cursor.close()
print  Done"

#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="localhost",  # your password
                     db="lam")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM silfexshipto where shipto ='556')

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

db.close()
