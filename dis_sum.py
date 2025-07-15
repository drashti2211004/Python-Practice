d1={'p':1100,'q':300,'r':600}
d2={'p':400,'q':200}

d3={}
for i,j in d1.items():
    for k,l in d2.items():
        if i==k:
            d3[i]=j+l

print(d3)





l=[16,62,24]
l1=[32,89,62]


l3={}

for i in range(len(l)):
    l3[l[i]]=l1[i]

print(l3)

