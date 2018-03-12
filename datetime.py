from flask import Flask, render_template
import datetime
import sqlite3 as mydb

app = Flask(__name__)
@app.route("/")
def hello():
 now = datetime.datetime.now()
 timeString = now.strftime("%Y-%m-%d %H:%M")
 templateData = {
 'title' : 'HELLO!',
 'time': timeString
 }
 return render_template('main.html', **templateData)

@app.route("/getInfo/<val>")
def info(val):
 now = datetime.datetime.now()
 if (val=="time"):
      con = mydb.connect('/home/pi/temperature.db')

      with con:
    
        cur = con.cursor()    
        cur.execute('SELECT * FROM TempData')

        rows = cur.fetchall()

        for row in rows:
           templateData = { 'date' : row }
           return render_template('finaltemp.html', **templateData)
          
          
         
 if (val=='date'):
     timeString = now.strftime("%Y-%m-%d")
     templateData = { 'title' : 'Starting and ending Dates',
         'name':'Enter Starting and Ending Date',
         'datetime': timeString}
 return render_template('date_time.html', **templateData)

if __name__ == "__main__":
 app.run(host='192.168.0.3', port=80, debug=True)
