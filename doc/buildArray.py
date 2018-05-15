from flask import Flask, render_template, request
import sqlite3 as sql
import csv
import json
app = Flask(__name__)

@app.route('/')
def Graph():

 filename = 'export.csv'
 datename = 'dates.csv'
 dates = []
 data = [] # This will contain our data
 # Create a csv reader object to iterate through the file
 reader = csv.reader( open( filename, 'rU'), delimiter=',', dialect='excel')
 row = reader.next() # Get the top row
 for row in reader: # Iterate the remaining rows
    data.append(row)


 reader1 = csv.reader( open( datename, 'rU'), delimiter=',', dialect='excel')
 row = reader1.next()
 for row in reader1:
     dates.append(row)

 newDates = [str(v[0]) for v in dates]
 newList = [float(x[0]) for x in data]
 print(newDates[0])
 return render_template("graph.html",newList=newList, newDates=newDates)

@app.route('/date')
def date():
   return render_template('date_time.html')

@app.route('/home')
def home():
   return render_template('SER_PJCT_Homepage.html')

@app.route('/login')
def login():
    return render_template('SER_PJCT_Login.html')


@app.route('/list', methods=['GET'])
def list():
   if request.method=="GET": 
       dateStart = "03/08/18"
        
       con = sql.connect("temperature.db")
       con.row_factory = sql.Row
       
       cur = con.cursor()
       cur.execute("SELECT date_time, TempF FROM TempData WHERE date_time BETWEEN ? AND ?", (request.args['dateRangeStart'], request.args['dateRangeEnd']))
       
       rows = cur.fetchall();
       return render_template("list.html",rows = rows)
    

if __name__ == "__main__":
   app.run(host='127.0.0.1', port=5000, debug=True)



