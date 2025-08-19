from think_databace import *
from tkinter import *
from tkint_login import *
from tkcalendar import DateEntry

def submitact():
    
    name1 = name.get()
    email1 = email.get()
    mobile1 = mobile.get()
    passw = password.get()
    cpassword1 = cpassword.get()
    gender1 = gender.get()
    hobby1 = hobby.get()
    DOB1 = DOB.get()
 
    print(f"The name entered by you is {name1} {email1} {mobile1} {passw} {cpassword1} {gender1} {hobby1} {DOB1}")
 
 

root = Tk()

root.geometry("1000x1000")
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

gender = Label(root,text="Enter a gender: ",font=("Arial",12,"bold"))
gender.place(x=50,y=300)

hobby = Label(root,text="Enter hobby: ",font=("Arial",12,"bold"))
hobby.place(x=50,y=350)

DOB = Label(root,text="Enter DOB: ",font=("Arial",12,"bold"))
DOB.place(x=50,y=400)

ename = Entry(root,bg="yellow")
ename.place(x=240,y=60)

eemail = Entry(root,bg="yellow")
eemail.place(x=240,y=110)

emobile = Entry(root,bg="yellow")
emobile.place(x=240,y=160)

epassword = Entry(root,bg="yellow")
epassword.place(x=240,y=210)

ecpassword = Entry(root,bg="yellow")
ecpassword.place(x=240,y=260)

gender_var=StringVar(value="female")
egender = Radiobutton(root, text='Male', variable=gender_var, value="male" ,font=("Arial",16,"italic"))
egender.place(x=240,y=300)
egender = Radiobutton(root, text='Female', variable=gender_var, value="female" ,font=("Arial",16,"italic"))
egender.place(x=340,y=300)

ehobby = Checkbutton(root, text='Reding',font=("Arial",16,"italic"))
ehobby.place(x=240,y=340)
ehobby1 = Checkbutton(root, text='Writing',font=("Arial",16,"italic"))
ehobby1.place(x=340,y=340)
ehobby2 = Checkbutton(root, text='Drawing',font=("Arial",16,"italic"))
ehobby2.place(x=440,y=340)
ehobby3 = Checkbutton(root, text='Music',font=("Arial",16,"italic"))
ehobby3.place(x=550,y=340)

edob = DateEntry(root, width=12, background='pink', foreground='white', borderwidth=2)
edob.place(x=240,y=400)

insert = Button(root,text="Insert",font=("Arial",16,"italic"),fg="red",command = submitact)
insert.place(x=50,y=500)

update = Button(root,text="update",font=("Arial",16,"italic"),fg="red")
update.place(x=140,y=500)

delete = Button(root,text="Delete",font=("Arial",16,"italic"),fg="red")
delete.place(x=240,y=500)

login = Button(root,text="Login",font=("Arial",16,"italic"),fg="red",command=login_screen)
login.place(x=330,y=500)

root.mainloop()
