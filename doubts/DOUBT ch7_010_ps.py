# WAP to print multiplication table of a number n using for loop in reverse order


n=int(input("Enter no here : \n"))

for i in range (11,1):
    print(f"{n} X {i} is {n*i}")