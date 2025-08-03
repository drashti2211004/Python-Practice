class Myclass:
    def myname(self):
        print("method 1!!")

class Myclass1(Myclass):
    def myname(self):
        super().myname()
        n = int(input("Enter Number:"))
        if n==0:
            print("Not even or Not odd")

        elif n%2 == 0:
            print("Even")

        else:
            print("odd")

obj = Myclass1()
obj.myname()