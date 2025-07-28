class A:
    def sudent1(self):
        self.a = input("Enter your Name: ")
        self.b = int(input("Enter Roll number: "))
        
        
class B(A):
    def sudent2(self):
        self.m = int(input("enter your Maths marks: "))
        self.s = int(input("enter youe Science marks: "))
        self.e = int(input("enter your English marks:"))
        

class C(B):
    def sudent3(self):
        total = self.m + self.s + self.e
        percent = total/3
        
        print(f"\nSudent nume: ",self.a)
        print(f"Sudent Roll number: ",self.b)

        print("Total :",total,"/300")
        print("Percentage: ",percent,"%")
        if percent>75:
            print("First Class")
        elif percent > 60:
            print("Second class")
        elif percent >=35:
            print("Pass")
        else:
            print("fail")

obj = C()
obj.sudent1()
obj.sudent2()
obj.sudent3()

       
