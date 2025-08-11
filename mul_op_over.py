class User:
    def __init__(self,a,b):
        print("Coustructor called !!")
        self.a=a
        self.b=b

    def __str__(self):
        return f"{self.a},{self.b}"

    def __mul__(self,obj):
        print("mul called !!")

        x = self.a * obj.a
        y = self.b * obj.b

        return x,y

obj = User (5,10)
print(obj)

obj1 = User (2,3)
print(obj1)


print("mul : ",obj*obj1)