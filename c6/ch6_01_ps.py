n1= int(input("Enter the number 1 you want : \n"))
n2= int(input("Enter the number 2 you want : \n"))
n3= int(input("Enter the number 3 you want : \n"))
n4= int(input("Enter the number 4 you want : \n"))

if (n1>n4):
    f1=n1
else:
    f1=n4

if (n2>n3):
    f2=n2
else:
    f2=n3

if (f1>f2):
    print("Greatest no. is", f1)
else:
    print("Greatest no. is", f2)

