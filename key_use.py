import sqlite3

def use_key(key):
    con = sqlite3.connect('maindb.db')
    cur = con.cursor()

    key_fomat = (key,)
    print(key)
    #getting codes
    codes = []
    for row in cur.execute("SELECT * FROM keys"):
        codes.append(row)
        print(row)
    #removing used key
    if key_fomat in codes:
        cur.execute("DELETE FROM keys WHERE key='{}'".format(key))
        con.commit()
    else:
        return False
    con.close()
    return True
