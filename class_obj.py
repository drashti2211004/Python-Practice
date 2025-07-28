class Myclass:
    def fun1(self):   #method
        l = [1,2,3,4,2,3,1,3,6,7,2,7,6,5,4]
        l1=[]
        for i in l:
            if i not in l1:
                l1.append(i)

        print(l1)

    def fun2(self):
        d={}

        for i in range(1,31):
            d[i]=i*i

        print(d)

    def fun3(self,a,b):
        print("addition:",a+b)

obj = Myclass()  #creation of object
obj.fun1()
obj.fun2()
obj.fun3(50,60)