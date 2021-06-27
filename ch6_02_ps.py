s1= int(input("Enter your marks in subject1 : \n"))
s2= int(input("Enter your marks in subject2 : \n"))
s3= int(input("Enter your marks in subject3 : \n"))

if (s1<33 or s2<33 or s3<33):
    print("You have failed")
elif ((s1+s2+s3)/3<40):
    print("You have failed as you didnt get 40 perc.")
else:
    print("You have passed")