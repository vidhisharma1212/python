n=int(input("Enter no. of rows here : \n"))
for i in range(n):
    print(" "*(n-i-1), end="")
    print("*"*(2*i+1), end="") 
    print(" "*(n-i-1))