import sqlite3

from flask import Flask
from flask import render_template
from key_use import use_key
import json
import threading

webapp = Flask(__name__)

key_list = ["123", "12345"]


def is_key(key):
    if(use_key(f'{key}')):
        return True
    else:
        return False


@webapp.route("/")
def start():
    return render_template('start.html')

@webapp.route("/abstimmung/")
def no_key():
    return "<H2>No Key Entered!!!</H2>"

@webapp.route("/abstimmung/<key>")
def enter(key):
    ok = is_key(key)

    if(ok):
        return render_template('map.html')
    else:
        return "<H2>You used an invalid key!!</H2>"

@webapp.route("/finish/<result>")
def finish(result):
    jsonresult = json.loads(result)
    for room in jsonresult:
        val = jsonresult[room]
        print(val)
    con = sqlite3.connect('maindb.db')
    cur = con.cursor()
    cur.execute("INSERT INTO result VALUES ('{}')".format(result))
    con.commit()
    con.close()

    return render_template("finsish.html")

@webapp.route("/results/")
def results():
    con = sqlite3.connect('maindb.db')
    cur = con.cursor()
    combresult = {
        "HU1":0,
        "HU2":0,
        "HU3":0,
        "HU4":0,
        "HU5":0,
        "HU6":0,
        "HU7":0,
        "HU8":0,
        "HU9":0,
        "HU10":0,
        "HU11":0,
        "HU12":0,
        "HU13":0,
        "HU14":0,
        "HU15":0,
        "HU16":0,
        "HU17":0,
        "AU1":0,
        "AU2":0,
        "AU3":0,
        "AU4":0,
        "MU1":0,
        "MU2":0,
        "MU3":0,
        "MU4":0,
        "MU5":0,
        "MU6":0,
        "MU7":0,
        "MU8":0,
        "MU9":0,
        "NU1":0,
        "NU2":0,
        "NU3":0,
        "NU4":0,
        "NU5":0,
        "NU6":0,
        "NU7":0,
        "NU8":0,
        "VU1":0,
        "VU2":0,
        "VU3":0,
        "VU4":0,
        "VU5":0,
        "VU6":0,
        "VU7":0,
        "VU8":0,
        "VU9":0,
        "VU10":0,
        "VU11":0,
        "HO1":0,
        "HO2":0,
        "HO3":0,
        "HO4":0,
        "HO5":0,
        "HO6":0,
        "HO7":0,
        "HO8":0,
        "HO9":0,
        "HO10":0,
        "HO11":0,
        "HO12":0,
        "HO13":0,
        "HO14":0,
        "HO15":0,
        "HO16":0,
        "HO17":0,
        "NO1":0,
        "NO2":0,
        "NO3":0,
        "NO4":0,
        "NO5":0,
        "NO6":0,
        "NO7":0,
        "VO1":0,
        "VO2":0,
        "VO3":0,
        "VO4":0,
        "VO5":0,
        "VO6":0,
        "VO7":0,
        "VO8":0,
        "VO9":0,
        "VO10":0,
        "VO11":0,
        "VO12":0,
        "VO13":0,
        "VO14":0,
        "ZU1":0,
        "ZU2":0,
        "ZU3":0,
        "ZU4":0,
        "ZU5":0,
        "ZU6":0,
        "ZU7":0,
        "ZU8":0,
        "ZU9":0,
        "ZU10":0,
        "ZU11":0,
        "ZU12":0,
        "ZU13":0,
        "ZU14":0,
        "ZU15":0,
        "ZU16":0,
        "ZU17":0,
        "ZU18":0,
        "ZU19":0,
        "ZU20":0,
        "ZU21":0,
        "ZU22":0,
        "ZU23":0,
        "ZU24":0,
        "ZU25":0,
        "ZU26":0,
        "ZU27":0,
        "ZU28":0,
        "ZU29":0,
        "ZU30":0,
        "ZU31":0,
        "ZU32":0,
        "ZO1":0,
        "ZO2":0,
        "ZO3":0,
        "ZO4":0,
        "ZO5":0,
        "ZO6":0,
        "ZO7":0,
        "ZO8":0,
        "ZO9":0,
        "ZO10":0,
        "ZO11":0,
        "ZO12":0,
        "ZO13":0,
        "ZO14":0,
        "ZO15":0,
        "ZO16":0,
        "ZO17":0,
        "ZO18":0,
        "ZO19":0,
        "ZO20":0,
        "KU1":0,
        "KU2":0,
        "KU3":0,
        "KU4":0,
        "KU5":0,
        "KU6":0,
        "KU7":0,
        "KU8":0,
        "KU9":0,
        "KU10":0,
        "KU11":0,
        "KU12":0,
        "KU13":0,
        "KU14":0,
        "KU15":0,
        "KU16":0,
        "SU1":0,
        "SU2":0,
        "SU3":0,
        "SU4":0,
        "SU5":0,
        "SU6":0,
        "SU7":0,
        "SU8":0,
        "SU9":0,
        "SU10":0,
        "SU11":0,
        "SU12":0,
        "SU13":0,
        "SU14":0,
        "SU15":0,
        "SU16":0,
        "SU17":0,
        "SU18":0,
        "SU19":0,
        "SU20":0,
        "SU21":0,
        "SU22":0,
        "SU23":0,
        "SU24":0,
        "SU25":0,
        "SU26":0,
        "SU27":0,
        "SU28":0,
        "SU29":0,
        "SU30":0,
        "SU31":0,
        "SU32":0,
        "SU33":0,
        "SU34":0
    }
    for result in cur.execute("SELECT * FROM result"):
        print(result)
        jsonresult = json.loads(result[0])
        for room in jsonresult:
            val = jsonresult[room]
            combresult[room] += val
    return render_template("result.html", results=combresult)
            


webapp.run()

#mittwoch 12:30