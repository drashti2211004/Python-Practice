d={1:"drashti",2:"krish",3:"hie"}
print(type(d))

d.get(1)  #returns key accoring to valus
print(d)

d.keys()    # returns  all keys
print(d)

d.update({4:"2",5:"3"})  # add the key and value

print(d)

d.values()   # returns  all values
print(d)

d.items()    # returns all pairs as tupls
print(d)

d.pop(2)     #delet 2 index 
print(d)

d.popitem()   # delet last item
print(d)

t=(1,2,3)
d1={}
print(d1.fromkeys(t,20))

