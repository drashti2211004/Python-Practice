class A:
    def fun1(self):
        print("method 1!!")

    def fun2(self):
        print("method 2!!")

class B(A):
    def fun3(self):
        print("method 3 !!")

obj = B()
obj.fun1()
obj.fun2()
obj.fun3()