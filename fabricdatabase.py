############################[ DATABSE  ]#######################

#importing modules.
from tkinter import *
import tkinter.ttk as ttk
import sqlite3


class Database:
    #initializes the class
    def __init__(self,db):        # creating a constructor
        self.conn =sqlite3.connect(db)    # creating a connection with sqlite3
        self.cur = self.conn.cursor()     # creating a cursor to send orders to database
            #if the table doesn't exist(means you have no database) then create it.
        self.cur.execute(
            ''' CREATE TABLE IF NOT EXISTS Fabric
                (LOTId integer PRIMARY KEY,
                Fabrictype text,
                Fabriclength float,
                Orderarrive text,
                Dispatched text,
                Totalpayment float,
                Shipped text)''')
        self.conn.commit()
        
        #selecting a record from the table
    def fetch(self):
        self.cur.execute("SELECT * FROM  Fabric")
        rows = self.cur.fetchall()
        return rows
        # insert a record in the database
    
    def insert(self,LOTId,Fabrictype,Fabriclength,Orderarrive,Dispatched,Totalpayment,Shipped):
    
        self.cur.execute('INSERT INTO Fabric VALUES(?,?,?,?,?,?,?,?,?,?)',
                          (LOTId,Fabrictype,Fabriclength,Orderarrive,Dispatched,Totalpayment,Shipped))
        self.conn.commit()    # commiting to providethe database confirmation regarding the changes made by a user or an application in the database
       
        #delete a record from the database
    def remove(self,LOTId):
        self.cur.execute("DELETE FROM Fabric WHERE LOTId =?",(LOTId,))
        self.conn.commit()
        
       
        #update a record from the database
    def update(self,LOTId,Fabrictype,Fabriclength,Orderarrive,Dispatched,Totalpayment,Shipped):
        self.cur.execute('''UPDATE Fabric SET
                            LOTId = ?,
                            Fabrictype = ?,
                            Fabriclength = ?,
                            Orderarrive = ?,
                            Dispatched = ?,
                            Totalpayment = ?,
                            Shipped = ?
                            where LOTId = ?''',
                         (LOTId,Fabrictype,Fabriclength,Orderarrive,Dispatched,Totalpayment,Shipped))
        self.conn.commit()
        #releases the instanace closing the database connection
    def __del__(self):
        self.conn.close()

#path where database will be saved and database file will be created.
path = 'C:/Users/Tayyaba Fatima/Desktop/fabricproject/'
db = Database(path + 'Fabrics.db')
