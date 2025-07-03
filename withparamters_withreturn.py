def fan(n):
    fac=1

    for i in range (1,n+1):
        fac*=i
    return fac

n=int(input("eneter your number: "))
print(fan(n))
