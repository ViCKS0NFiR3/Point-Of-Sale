import mysql.connector

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='userlogin'
)
mycursor = mydb.cursor()
#mycursor.execute("SELECT * FROM userinfo;")
#row = mycursor.fetchall()
#print(row)
def createUser():
    name = input("Enter your Name: ")
    Uname = input("Enter username: ")
    pWord = input("Enter password: ")

    mycursor.execute("INSERT INTO userinfo (name,uname,pWord) VALUES (%s,%s,%s)",(name,Uname,pWord))

    mydb.commit()

Uname = input("username: ")
pWord = input("password: ")
mycursor.execute("SELECT uname, pWord FROM userinfo WHERE uname = %s AND pWord = %s;",(Uname,pWord))
x = mycursor.fetchall()

if x:
    print("Hello")
else:
    print("Invalid username or password")





