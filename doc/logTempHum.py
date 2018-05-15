#!/usr/bin/python
import os
import time
import sqlite3 as sql
import sys
import Adafruit_DHT
""" Log Current Time, Temperature in Celsius and Fahrenheit
    To an Sqlite3 database"""

def readTemp():
    tempfile = open("/sys/bus/w1/devices/28-00000697555d/w1_slave")
    tempfile_text = tempfile.read()
    currentTime=time.strftime('%x')
    tempfile.close()
    tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
    tempF=tempC*9.0/5.0+32.0
    
    sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
    if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
        sensor = sensor_args[sys.argv[1]]
        pin = sys.argv[2]
    else:
        print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
        print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
        sys.exit(1)
    
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    return [currentTime, tempC, tempF, humidity]

def logTemp():
    con = mydb.connect("tempHum.db")
    with con:
            try:
                [t,C,F,H]=readTemp()
                print ("Current temperature is: %s F" %F)
                print ("Humidity logged %s " %H)
                cur = con.cursor()
                cur.execute('insert into TempHumData values(?,?,?,?)', (t,C,F,H))
                
            except:
                print "Error!"    
            

logTemp()
