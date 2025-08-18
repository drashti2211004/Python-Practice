from tkinter import *

def login_screen():
    root=Tk()

    root.geometry("500x500")
    root.title("Login From")

    email = Label(root,text="Enter email: ",font=("Arial",12,"bold"))
    email.place(x=100,y=80)

    eemail = Entry(root,by="yellow")
    eemail.place(x=240,y=110)

    password = Label(root,text="Enter password: ",font=("Arial",12,"bold"))
    password.place(x=50,y=200)

    epassword = Entry(root,by="yellow")
    epassword.place(x=240,y=210)

    login = Button(root,text="Login",font=("Arial",16,"italic"),fg="red")
    login.place(x=330,y=330)

    root.mainloop()