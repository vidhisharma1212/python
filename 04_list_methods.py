L1= [1, 8, 7, 2, 21, 15]
# L1_sorted= L1.sort() #this way is wrong. you need not put another variable in code to sort out something
# print(L1_sorted)

# # do this instead----
# L1.sort()
# print(L1)

L1.reverse()
print(L1)

L1.append(32)
print(L1)

L1.insert(0,544)
print(L1)

L1.pop(3) # removes value of 3rd index
print(L1)

L1.remove(7) # removes the value 7 from the list
print(L1)