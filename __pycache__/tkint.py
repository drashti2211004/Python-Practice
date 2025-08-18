
from tkinter import *
#from login1 import *
root = Tk()

root.geometry("500x500")
root.title("Signup From")

name = Label(root,text="Enter Name: ",font=("Arial",12,"bold"))
name.place(x=50,y=50)

email = Label(root,text="Enter email: ",font=("Arial",12,"bold"))
email.place(x=50,y=100)

mobile = Label(root,text="Enter mobile: ",font=("Arial",12,"bold"))
mobile.place(x=50,y=150)

password = Label(root,text="Enter password: ",font=("Arial",12,"bold"))
password.place(x=50,y=200)

cpassword = Label(root,text="Enter cpassword: ",font=("Arial",12,"bold"))
cpassword.place(x=50,y=250)

ename = Entry(root,by="yellow")
ename.place(x=240,y=60)

eemail = Entry(root,by="yellow")
eemail.place(x=240,y=110)

emobile = Entry(root,by="yellow")
emobile.place(x=240,y=160)

epassword = Entry(root,by="yellow")
epassword.place(x=240,y=210)

ecpassword = Entry(root,by="yellow")
ecpassword.place(x=240,y=260)

insert = Button(root,text="Insert",font=("Arial",16,"italic"),fg="red")
insert.Place(x=50,y=130)


update = Button(root,text="update",font=("Arial",16,"italic"),fg="red")
update.place(x=140,y=330)

delete = Button(root,text="Delete",font=("Arial",16,"italic"),fg="red")
delete.place(x=240,y=330)

login = Button(root,text="Login",font=("Arial",16,"italic"),fg="red")
login.place(x=330,y=330)

root.mainloop()
