# def greatest_number(n1,n2,n3):
#     if n1>n2:
#         great=n1
#     else:
#         great=n2
#     if great>n3:
#         greatest=great
#     else:
#         greatest=n3 
#     return greatest



def max(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
        else:
            return n3
    else: 
        if n2>n3:
            return n2
        else:
            return n3

j1=int(input("Enter no. 1 : \n"))
j2=int(input("Enter no. 2 : \n"))
j3=int(input("Enter no. 3 : \n"))

# greatest_no= greatest_number(j1,j2,j3)
greatest_no= max(j1,j2,j3)
print(greatest_no)