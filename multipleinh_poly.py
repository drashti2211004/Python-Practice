class myclass():
    def fun(self):
        print("method 1!!")

class myclass1():
    def fun(self):
        super().fun()
        print("method 2!!")

class myclass2(myclass1,myclass):
    def fun(self):
        super().fun()
        print("method 3!!")

obj = myclass2()
obj.fun()

