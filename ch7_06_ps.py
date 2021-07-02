#  factorial.. -----> 
# n! = 1 X 2 X 3 X 4 X 5 X 6 ....n
# 5!= 1 X 2 X 3 X 4 X 5 = 1x 120= 120
# 2! = 1 X 2 = 2

n= int(input("Enter the number here : \n"))

factorial= 1
for i in range(1, n+1):
    factorial = factorial*i
# else:
    # print(factorial) # methods tried by me

print(f"The factorial of {n} is {factorial}")