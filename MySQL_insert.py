# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:15:54 2019

@author: ALR203
"""


import mysql.connector
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
SQL_DATABASE = 'EXAMPLEDATABASE'
SQL_USER = 'EXAMPLEUSER'
SQL_PASSWORD = 'EXAMPLEPASS'
SQL_HOST = 'localhost'


roomNum = '.'
bCode = 'test'
dep = 'test'
sqFt = '0'
roomType = 'test'
seatCount = '0'
seatType = 'test'
seatConfig = 'test'
model = 'test'
blinds = 'test'
compSeats = '0'

cnx = mysql.connector.connect(
        user= SQL_USER, database= SQL_DATABASE, password = SQL_PASSWORD, host=SQL_HOST)
cursor = cnx.cursor(buffered=True)

top = Tk()

L1 = Label(top, text="RoomNum")
L1.pack()
E1 = Entry(top, bd=5)
E1.pack()

L2 = Label(top, text="bCode")
L2.pack()
E2 = Entry(top, bd=5)
E2.pack()

L3 = Label(top, text="sqFt")
L3.pack()
E3 = Entry(top, bd=5)
E3.pack()

L4 = Label(top, text="roomType")
L4.pack()
E4 = Entry(top, bd=5)
E4.pack()

L5 = Label(top, text="seatCount")
L5.pack()
E5 = Entry(top, bd=5)
E5.pack()

L6 = Label(top, text="seatType")
L6.pack()
E6 = Entry(top, bd=5)
E6.pack()

L7 = Label(top, text="seatConfig")
L7.pack()
E7 = Entry(top, bd=5)
E7.pack()

L8 = Label(top, text="model")
L8.pack()
E8 = Entry(top, bd=5)
E8.pack()

L9 = Label(top, text="blinds")
L9.pack()
E9 = Entry(top, bd=5)
E9.pack()

L10 = Label(top, text="compseats")
L10.pack()
E10 = Entry(top, bd=5)
E10.pack()

L11 = Label(top, text="dep")
L11.pack()
E11 = Entry(top, bd=5)
E11.pack()

L12 = Label(top, text='no input')
L12.pack()

def submitData():
    global roomNum
    global bCode
    global dep
    global sqFt
    global roomType
    global seatCount
    global seatType
    global seatConfig
    global model
    global blinds
    global compSeats
    roomNum = E1.get()
    bCode = E2.get()
    dep = E11.get()
    sqFt = E3.get()
    roomType = E4.get()
    seatCount = E5.get()
    seatType = E6.get()
    seatConfig = E7.get()
    model = E8.get()
    blinds = E9.get()
    compSeats = E10.get()
    insert = ("""
    INSERT INTO room_info (
    room_num,
    building_code,
    department,
    sq_feet,
    room_type,
    seat_count,
    seat_type,
    seat_config,
    projector_model,
    blinds,
    computer_seats
    )
    VALUES ( """ +
    "'"+roomNum+"',"+
    "'"+bCode+"',"+
    "'"+dep+"',"+
    ""+sqFt+","+
    ""+roomType+","+
    ""+seatCount+","+
    "'"+seatType+"',"+
    "'"+seatConfig+"',"+
    "'"+model+"',"+
    "'"+blinds+"',"+
    ""+compSeats+")"+
    "ON DUPLICATE KEY UPDATE "+
    "building_code= '"+bCode+"',"
    "department= '"+dep+"',"
    "sq_feet= "+sqFt+","
    "room_type= "+roomType+","
    "seat_count= "+seatCount+","
    "seat_type= '"+seatType+"',"
    "seat_config= '"+seatConfig+"',"
    "projector_model= '"+model+"',"
    "blinds= '"+blinds+"',"
    "computer_seats= "+compSeats+";"
    )
    checkInsert = "SELECT * FROM room_info WHERE building_code= '" +bCode+"'"
    "AND department= '"+dep+"'"
    "AND sq_feet= "+sqFt+""
    "AND room_type= "+roomType+""
    "AND seat_count= "+seatCount+""
    "AND seat_type= '"+seatType+"'"
    "AND seat_config= '"+seatConfig+"'"
    "AND projector_model= '"+model+"'"
    "AND blinds= '"+blinds+"'"
    "AND computer_seats= "+compSeats+"LIMIT 0, 1;"
    print(insert)
    cursor.execute(insert)
    cursor.reset()
    cnx.commit()
    L12.config(text='Successful',bg='green')

submitButton = Button(top, text="submit", command=submitData)
submitButton.pack()
top.mainloop()




cursor.close()
cnx.close()
