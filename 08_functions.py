'''marks= [42,32,12,54]
percent= ((sum(marks)/400)*100)
print(percent)

marks2= [42,32,12,54]
percent= ((sum(marks2)/400)*100)
print(percent)'''

# however, one must not use it, as there are functions to help one out!

def percent(marks):
    return((sum(marks)/400)*100)

marks1= [42,32,12,54]
percent1= percent(marks1)

marks2= [52,98,24,54]
percent2= percent(marks2)

print(percent1, percent2)

def sum(n1,n2):
    return n1+n2

s= sum(2,3)
print(s)