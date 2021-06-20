b= set()
print(type(b))

'''
ADDING A VALUE
'''
b.add(3)
b.add("An apple")
b.add(78)
b.add("An apple")
# b.add([1,2,3,4,5]) # can't enter a list in a set as it may be changed
b.add((1,2,3,4,5)) # a tuple can be added
# b.add({ 1: "a number"}) # cant add a list as it can be changed
print(b)

'''
LEN OF SET
'''
print(len(b)) # to print the length 

'''
REMOVAL OF AN ELEMENT FROM SET
'''
b.remove(3) # this will remove 3 from set
# b.remove(43) # cant remove an element which is not there in set, will throw an error 
print(b)

'''
pop function
'''
print(b.pop()) # to remove an element randomly from the set, and returns the deleted value
print(b)

'''
CLEAR SET
'''
print(b.clear())
