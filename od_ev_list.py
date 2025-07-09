l=[]
n=int(input("Enter your len: "))
for i in range(1,n+1):
    a=input("ENter your number: ")
    l.append(a)

print(l)

a=len(l)
for i in range(0,a):
    for j in range(i+1,a):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
for i in range(0,a):
    print("ASD Order:",l[i])


