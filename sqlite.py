from flask import Flask, render_template
import datetime
import sqlite3 as mydb
import sys

app = Flask(__name__)
@app.route("/")

def List():

    con = mydb.connect('/home/pi/temperature.db')

    with con:
    
        cur = con.cursor()    
        cur.execute('SELECT * FROM TempData')
    
        data = cur.fetchall()
    
        for row in data:
            print row

