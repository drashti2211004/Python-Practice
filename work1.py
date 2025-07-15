
while True:
    menu="""
    press 1 for squres
    press 2 for merge dict
    press 3 for marge list
    press 4 for exit
"""
    print(menu)
    choice=int(input("entrr choice: "))

    if choice==1:
        
        d=int(input("enter your number: "))
        n={}
        for i in range(1,d+1):
            n[i]=i*1
        
        print(n)
    
    
    elif choice==2:
            d1={'p':1100,'q':300,'r':600}
            d2={'p':400,'q':200} 
            d3={} 
            for i,j in d1.items():
                for k,l in d2.items(): 
                    if i==k:             
                        d3[i]=j+l
            print(d3)
               

    elif choice==3:
        l=[16,62,24]
        l1=[32,89,62]
        l3={}
        
        for i in range(len(l)):
            l3[l[i]]=l1[i]

        print(l3)       

    elif choice==4:
        print("Thank you !!")
        break

    else:
        print("Invalid choce !!")
        break


