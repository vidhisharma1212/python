def stars(n):
    for i in range(n+1):
        print("*" * (n-i))

j=int(input("Enter no. of stars : \n"))
print(stars(j))
