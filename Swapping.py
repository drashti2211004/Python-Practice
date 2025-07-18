      #swapping

a=int(input("Enter your Number a: "))
b=int(input("Enetr your Number b: "))
  #a=30 b=20
  
  #with used 3 value
temp=a  #temp=30 a=black
a=b     #a=20 b=black
b=temp  #b=30 temp=black


  # without used variable
a=a+b  #30+20=50(a)
b=a-b  #50-20=30(b)
a=a-b  #50-30=20(a)

print("After Swapping value of A:",a)
print("After Swapping value of B:",b)