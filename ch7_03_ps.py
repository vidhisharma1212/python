n= int(input("Enter the numbere here : \n"))
prime= True
for i in range(2,n):
    if (n%i==0):
        prime=False
        break
    print("this number isn't prime")
else:
    print("this number is prime.")
