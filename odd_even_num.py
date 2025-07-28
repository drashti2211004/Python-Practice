i=1
even=0
odd=0
evsum=0
odsum=0
sum=0

while(i<=5):
    n=int(input("Enter your Number :"))
    if n%2==0:
        print(n,"is event number.")
        even+=1
        evsum+=n
    else:
        print(n,"is odd number")
        odd+=1
        odsum+=n
    sum+=n
    i=i+1

print("even number count",even)
print("odd number count",odd)
print("even sum",evsum)
print("odd sum",odsum)
print("total sum",sum)