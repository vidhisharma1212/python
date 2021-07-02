lang= {}
a= input("Enter your favourite language a : ")
b= input("Enter your favourite language b : ")
c= input("Enter your favourite language c : ")
d= input("Enter your favourite language d : ")
e= input("Enter your favourite language e : ")

lang['a']= a
lang['a']= b # here, repetetion, thus value of a 's choice will update from a to b
lang['b']= b
lang['c']= c
lang['d']= d

print(lang)

# u= {
#     "a": a,
#     "b": b,
#     "c": c,
#     "d" : d
# }
# lang.update(u)

# m={
#     "e" : e
# }
# lang.update(m)
# print(lang)