import sqlite3;
import pandas as pd;


con=None

def getConnection():
    databaseFile="hw3.db"
    global con
    if con == None:
        con=sqlite3.connect(databaseFile)
    return con

def createTable(con):
    try:
        c = con.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS people
                  (id integer primary key, FirstName varchar, LastName varchar)""")
    except Exception as e:
        pass

def insert_somedata(con):
    c = con.cursor()
    c.execute("""INSERT INTO people (ID, FirstName, LastName)
              values(1, 'wang0', 'erxiao')""")
    c.execute("""INSERT INTO people (ID, FirstName, LastName)
              values(2, 'wang1', 'hong')""")
    c.execute("""INSERT INTO people (ID, FirstName, LastName)
              values(3, 'wang2', 'ming')""")
    c.execute("""INSERT INTO people (ID, FirstName, LastName)
              values(4, 'wang3', 'ming')""")


def queryExec():
    con=getConnection()
    createTable(con)
    insert_somedata(con)
    # r = con.execute("""SELECT * FROM people""")
    result=pd.read_sql_query("select LastName, count(*) from people group by LastName HAVING count(*)>1 ;",con)
    return result


r = queryExec()
print(r)
