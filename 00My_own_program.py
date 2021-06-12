name= input("Enter your name in this box : ")
year= input("Which year were you born at ?")
year= int(year)
age= 2021-year
if age<18:
    print("Sorry! You are underage!")
if age>= 18:
    print("Welcome", name )
    print(" Ready to start this game?")
readyornot= input("Enter 'Yes' to proceed : ")
if readyornot!='Yes':
    print("okay, then we will wait for you...!")
if readyornot=='Yes': 
    print("let's go!") 



