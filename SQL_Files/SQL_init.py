##
##  This file will ininulize the SQL Database File
##
import mysql.connector

def Init_Database():
    # Creating connection object
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "dhED26dL"
    )
    
    # Printing the connection object
    print(mydb)

    # Creating an instance of 'cursor' class
    # which is used to execute the 'SQL'
    # statements in 'Python'
    cursor = mydb.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS NewsAnalyzer;")

    cursor.execute("USE NewsAnalyzer")
    # cursor.execute("CREATE TABLE UserInfo (name VARCHAR(255), password VARCHAR(255))")