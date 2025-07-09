a=[1, 2, 3, 1, 2, 4, 5, 6, 5]
a1=[]
a2=[]
print(len(a))
for i in a:
        if i not in a1:
            a1.append(i)
        else:
            a2.append(i) 
print(a1)
print(a2)