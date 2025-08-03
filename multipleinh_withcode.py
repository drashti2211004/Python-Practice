# class myclass():
#     def fun1(self):
#         print("method 1!!")

# class myclass1():
#     def fun2(self):
#         print("method 2!!")

# class myclass2(myclass,myclass1):
#     def fun3(self):
#         print("method 3!!")

# obj = myclass2()
# obj.fun1()
# obj.fun2()
# obj.fun3()


class Class1:  
    def sum(self,a,b):  
        return a+b;  

class Class2:  
    def mul(self,a,b):  
        return a*b;  

class Class3(Class1,Class2):  
    def divide(self,a,b):  
        return a/b;  

obj = Class3()  

print(obj.sum(10,20))
print(obj.mul(10,7))
print(obj.divide(10,5))