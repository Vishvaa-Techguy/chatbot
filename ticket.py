from random import randint
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vishvaa_vsk",auth_plugin='mysql_native_password',
  database = "booking_system"
)

while True:
    input_ = input("Enter the word: ")
    if input_ == "get":
        ticket = f"IRT{randint(100000,999999)}"
        mno = randint(1000000000,9999999999)
        print(mno,ticket)
        cur = mydb.cursor()
        cur.execute(f"insert into ticket(mobile_number,ticketID) values('{mno}','{ticket}');")
        mydb.commit()
    else:
        break