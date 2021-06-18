b= set()
print(type(b))

'''
ADDING A VALUE
'''
b.add(3)
b.add("An apple")
b.add(3)
b.add("An apple")
# b.add([1,2,3,4,5]) # can't enter a list in a set as it may be changed
b.add((1,2,3,4,5)) # a tuple can be added
# b.add({ 1: "a number"}) # cant add a list as it can be changed
print(b)

'''
LEN OF SET
'''
print(len(b)) # to print the length 

b.remove(13)
print(b)