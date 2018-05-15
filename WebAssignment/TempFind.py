from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('date_time.html')

@app.route('/list', methods=['GET'])
def list():
   if request.method=="GET": 
        
       con = sql.connect("temperature.db")
       con.row_factory = sql.Row
       
       cur = con.cursor()
       cur.execute("SELECT * FROM TempData WHERE date_time BETWEEN ? AND ?", (request.args['dateRangeStart'], request.args['dateRangeEnd']))
       
       rows = cur.fetchall();
       return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5000, debug = True)