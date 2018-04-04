#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 22:58:26 2018; @author: mh70
"""

import sqlite3

def create_tables():
    conn = sqlite3.connect("Alchemy_Data_Bank.dat")
    c = conn.cursor()
    
    c.execute("""
    CREATE TABLE IF NOT EXISTS recipie(id, name, iid_1, iid_2, iid_3);
    """)
    
    c.execute("""
    CREATE TABLE IF NOT EXISTS ingredient(id, name);
    """)
    conn.commit()
    c.close()
    conn.close()
    

def insert_records():
    conn = sqlite3.connect ("Alchemy_Data_Bank.dat")
    c = conn.cursor()
    idata=[(0,"Salami"),
           (1,"Pasta"),
           (2,"Oil"),
           (3,"Olive"),
           (4,"Funghi"),           
           ]
    
    rdata=[(0,"Recipie1",0,1,1),
           (1,"Recipie2",4,1,3),
           (2,"Recipie3",2,1,1),
           (3,"Recipie4",3,4,1),
           (4,"Recipie5",1,2,3),
    ]
        
    c.executemany("insert into recipie(id, name, iid_1, iid_2, iid_3) values (?,?,?,?,?)", rdata)
    c.executemany("insert into ingredient(id, name) values (?,?)", idata)
    conn.commit()
    c.close()
    conn.close()

def select_all_rows():
    conn = sqlite3.connect ("Alchemy_Data_Bank.dat")
    c = conn.cursor()
    qry1 = """select name,  
        (select name from ingredient where ingredient.id = recipie.iid_1), 
        (select name from ingredient where ingredient.id = recipie.iid_2), 
        (select name from ingredient where ingredient.id = recipie.iid_3)
        from recipie;"""
    
    rsl = c.execute(qry1)
    for r in rsl:
        print (r)
    
    c.close()
    conn.close()
    
def select_rows(rec_names):
    conn = sqlite3.connect ("Alchemy_Data_Bank.dat")
    c = conn.cursor()
    qry2 = """select name,  
        (select name from ingredient where ingredient.id = recipie.iid_1), 
        (select name from ingredient where ingredient.id = recipie.iid_2), 
        (select name from ingredient where ingredient.id = recipie.iid_3)
        from recipie
        where name = ?;"""
    
    for rec_name in rec_names:
        #a single member tupple requires a trailing comma
        rsl = c.execute(qry2, (rec_name,)) 
        for r in rsl:
            print (r)
    
    c.close()
    conn.close()   
    
#create_tables() #run once
#insert_records() #run once

print("all rows: " )
select_all_rows()

print ("\nselected rows in the argument:")
select_rows(("Recipie3", "Recipie4"))

print ("\nselected row in the argument:"
       "\n(note that a single member tupple requires a trailing comma)")
select_rows(("Recipie3",))

rec_names = ("Recipie1", "Recipie2")
print("\nselected rows " + str(rec_names) + " : ")
select_rows(rec_names)
 















def insert_records_x():
    conn = sqlite3.connect ("Alchemy_Data_Bank.dat")
    c = conn.cursor()
    idata=[(0,"Ingredient1"),
            (1,"Ingredient2")]
    
    rdata=[(0,"Recipie1",0,1,1)]
        
    c.executemany("insert into recipie(id, name, iid_1, iid_2, iid_3) values (?,?,?,?,?)", rdata)
    c.executemany("insert into ingredient(id, name) values (?,?)", idata)
    conn.commit()
    c.close()
    conn.close()
    
def xyz(rec_names):
    for r in rec_names:
        print(r)
        
        
        