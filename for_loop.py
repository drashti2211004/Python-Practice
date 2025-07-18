# increment method
# for i in range(1,11,1):
#     print(i)

#  decrement method
# for i in range(10,0,-1):
#     print(i)

# #user method
# n=int(input("enetr your number: "))
# for i in range(1,n+1):
#     print(i)


ev=0
od=0
evsum=0
odsum=0
sum=0
for i in range(1,6):
    n=int(input("enter your number: "))

    if n%2 == 0:
        print(n,"is event")
        ev+=1
        evsum+=n
    else :
        print(n,"is odd")
        od+=1
        odsum+=n
    sum+=n

print("event count",ev)
print("odd count",od)
print("event sum",evsum)
print("odd sum",odsum)
print("sum",sum)
