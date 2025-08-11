import pymysql

mydb = pymysql.connect(host="localhost" ,user="root" ,password="")
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS signup")
mydb.commit()

mydb = pymysql.connect(host="localhost" ,user="root" ,password="" ,database="signup")
mycursor = mydb.cursor()

mycursor.execute("create table if not exists data(id int primary key auto_increment ,name varchar(100),subject varchar(40))")
mydb.commit()