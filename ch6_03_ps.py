text= input("Enter the text you want to input \n" )

# if ("make a lot of money" or "buy now" or "subscribe this" or "click this" in text) :
'''
the following is better and fast running than the above one (commented the above)
'''
if ("make a lot of money" in text): 
    spam= True
elif ("buy now" in text): 
    spam= True
elif ("subscribe this" in text): 
    spam= True
elif ("click this" in text): 
    spam= True
else :
    spam= False

if(spam):
    print("This text is spam.")
else:
    print("This text is not spam.")