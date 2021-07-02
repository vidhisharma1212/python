x= int(input("Enter your grades here : \n"))

if 90<=x<=100 :
    print("Grade: Excellent")
elif 80<=x<90 :
    print("Grade: A")
elif 70<=x<80 :
    print("Grade: B")
elif 60<=x<70 :
    print("Grade: C")
elif 50<=x<60 :
    print("Grade: D")
else :
    print("Grade: F")




# Now, other method can be-
if x>=90 :
    grade='Ex'
elif x>=80 :
    grade='A'
elif x>=70 :
    grade='B'
elif x>=60 :
    grade='C'
elif x>=50 :
    grade='D'
else :
    grade='F'
print("Your grade is : " + grade)
print("Your grade is : ",grade)