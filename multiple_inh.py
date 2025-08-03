class myclass():
    def fun1(self):
        print("method 1!!")

class myclass1():
    def fun2(self):
        print("method 2!!")

class myclass2(myclass,myclass1):
    def fun3(self):
        print("method 3!!")

obj = myclass2()
obj.fun1()
obj.fun2()
obj.fun3()