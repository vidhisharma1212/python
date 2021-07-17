#  letter template
letter= '''Dear <|NAME|>
Warm wishes from XYZ Academy! We're happy to share with you, the result of your 
previous given exams. 
You are selected !

We wish you are great day ahead!
Thank you
Vidhi
Date: <|DATE|>
'''


name1= input("Enter name of the employee : \n")
date= input("Enter date here: \n ")
letter =letter.replace("<|NAME|>", name1)
letter= letter.replace("<|DATE|>", date)
print(letter)