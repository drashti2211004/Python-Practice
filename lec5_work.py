    # patten in left side rivers 

for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


    # patten in right side rivers 

for i in range(6,0,-1):
    for k in range(0,6-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()


    # pyramid in rivers

for i in range(6,0,-1):
    for k in range(0,6-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(" *",end=" ")
    print()


    # diamond

for i in range(1,7):
    for k in range(1,7-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(" *",end=" ")
    print()
for i in range(6,0,-1):
    for k in range(0,6-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(" *",end=" ")
    print()

        
    #or

for i in range(1,6):
    print(" "*(6-i)," *"*i)
for i in range(5,0,-1):
    print(" "*(6-i)," *"*i)