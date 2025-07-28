l=[1,2,3,"drashti","hello","hiee up",True,5000,3000,False,1,1,1]
print(type(l))

l.append(100)     # Adds an element at the end of the list
print(l)

print(l.count(1))      # count the number of elements with the specified value

print(l.index("drashti"))   # Returns the index of the first element with the specified value

l.insert(4,"parth")    # Adds an element at the specified position index
print(l)

l.pop(5)     # Removes the element at the specified position index
print(l)

l.remove(2)    # Removes the last item with list
print(l)

l.reverse()    # Reverses the order of the list
print(l)
