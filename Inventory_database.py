import pymysql

mydb = pymysql.connect(host="localhost" ,user="root" ,password="")
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS Inventory")
mydb.commit()

mydb = pymysql.connect(host="localhost" ,user="root" ,password="" ,database="Inventory")
mycursor = mydb.cursor()

mycursor.execute("create table if not exists manager1(id INT PRIMARY KEY AUTO_INCREMENT ,name varchar(100),price DECIMAL(10,2),quantity INT)")
mydb.commit()

mycursor.execute("create table if not exists customer(id INT PRIMARY KEY AUTO_INCREMENT ,name varchar(100),price DECIMAL(10,2),quantity INT)")
mydb.commit()

