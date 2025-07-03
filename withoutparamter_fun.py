# functions 1: function without parameters and without return type

import math

def signup():
    for i in range(1,6):
        print("*"*i)

def fac():
    n=int(input("Enter your Number: "))
    print(math.factorial(n))

signup() #call
fac() #call