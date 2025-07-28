class Prime:
    def prime(self):
        n=int(input("Enter your number: "))
        if n<=0:
            print("enter Positive number")
        else:
            if n==1 or n==2 or n==3:
                print("prime")
            else:
                prime=0
                for i in range(1,n+1):
                    if(n%1==0):
                        prime+=1
                if prime==2:
                    print(n,"is a prime number")
                else:
                    print(n,"not a prime number")

class Patten:
    def patten(self):
        for i in range(1,6):
            for j in range(1,i+1):
                print("*",end=" ")
            print()



class Table:
    def table(self):
        n = int(input("enter your number:"))

        for i in range(1,11):
            print(f"{n}*{i}={n*i}")


class Reverse:
    def rev(self,s):
        if len(s)%2==0:
            print(s)

        else:
            mid = len(s)//2
            print(s[mid-1]+s[mid]+s[mid+1])
            return mid 
