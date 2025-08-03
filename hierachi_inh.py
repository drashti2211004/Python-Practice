class myclass():
    def fun1(self):
        print("method 1!!")

class myclass1(myclass):
    def fun2(self):
        print("method 2!!")

class myclass2(myclass):
    def fun3(self):
        print("method 3!!")

obj = myclass1()
obj1 = myclass2()

obj.fun1()
obj.fun2()
obj1.fun3()