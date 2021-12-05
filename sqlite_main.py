import sqlite3 as database

con = database.connect('maindb.db')
cur = con.cursor()

def talk_toData():
    q = "{}".format(input('SQL: '))
    print(q)
    print(cur.execute(q))
    con.commit()
#"INSERT INTO keys VALUES ('123')"
#'SELECT * FROM keys'

def show():
    for row in cur.execute("SELECT * FROM keys"):
        print(row)

talk_toData()
con.close()