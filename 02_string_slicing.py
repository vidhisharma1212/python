greeting= "Good morning, "
name= "Sharma "
print(type(name))
# Concatenating two strings
print( greeting+name)
name= "Sharma"
print(name[3])
# name[3]= "d" --> Does not work
print(name[0:3])
print(name[:3]) # is as same as print(name[0:3])
print(name[0:]) # is as same as print(name)  , means, prints full
print(name[-1:-5]) 

d = name[1:4:1] # with a skip value of 1 ---> every 1st charcater selected
print(d)

d1 = name[1:4:2] # with a skip value of 2 ---> every 2nd charcater selected
print(d1)

name1= "SharmaIsNice" # length= 12
name2= "0123456789"   # length= 10
e= name2[0:12:2] #----> all numbers divisible by 2 (every 2nd) { Here, 2= skip value }
print(e)
'''
skip value= no. of characters skipped+1
or
no. of skipped characters = skip value- 1
'''
f= name2[0:10:3] #----> all numbers divisible by 3 (every 3rd) { Here, 3= skip value }
print(f) 
