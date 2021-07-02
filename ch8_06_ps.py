def inches_to_cms(n):
    return (n*2.54)
j=float(input("Enter length in cm : \n"))
if inches_to_cms(j)==1:
    print(inches_to_cms(j),"inch")
else:
    print(inches_to_cms(j),"inches")