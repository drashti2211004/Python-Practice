class myclassA():
    def fun1(self):
        print("method 1!!")

class myclassB(myclassA):
    def fun2(self):
        print("method 2!!")

class myclassC():
    def fun3(self):
        print("method 3!!")


class myclassD(myclassB,myclassC):
    def fun4(self):
        print("method 4!!")

obj = myclassD()

obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()