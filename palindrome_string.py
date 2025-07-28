# def string_palindrome(s):
#     rev=s[::-1]

#     if s==rev:
#         print("palindrome !!")
#     else:
#         print("not palindrome !!")

# s=input("Enter name: ")
# string_palindrome(s)

def slicing_mid(s):
    if len(s)%2==0:
        print(s)
    else:
        mid=len(s)//2
        print(s[mid-1]+s[mid]+s[mid+1])
s=input("enter your string: ")
slicing_mid(s)