def sum_recursive(n):
    for i in range(n+1):
        sum= (n-1)+n
        return sum

j=int(input("Enter the number : \n"))
s=sum_recursive(j)
print(s)