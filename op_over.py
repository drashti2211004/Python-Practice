# # defult

class User:
    def __init__(self):
        print("Constructor called !!")

obj = User()


# parameters 

class User:
    def __init__(self,a,b):
        print("parameters Coustructor called !!")
        self.a=a
        self.b=b

    def __str__(self):
        return f"{self.a},{self.b}"

obj = User (10,20)
print(obj)
