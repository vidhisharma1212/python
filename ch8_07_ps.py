# def strip(an):
#     for i in (an):
    
#         if an[i] is 'word':
#             an.replace('word','    ')
#             print(an.strip())
#         else:
#             print(an)
# hi=input("Enter a sentence here : \n")
# strip(hi)

def new_string(thing, word):
    n= thing.replace(word, "")
    return n.strip()
    # return n
si=input("Enter a sentence here : \n")
restri=input("Enter the word here : \n")
c= new_string(si,restri)
print(c)