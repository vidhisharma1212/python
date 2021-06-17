myDictionary = {
    "fast": "In a quick mannner",
    "notebook" : "A book with a set of pages to write down something",
    "score" : [1,2,3,5,],
    "anotherdictionary" : { "phone" : "a device to check mails, calls, etc"},
    1 : 2
}

# Dictionary methods
# print(type(myDictionary.keys())) # Printing keys of the dictionary
# print(list(myDictionary.keys())) # Printing keys of the dictionary
# print(myDictionary.values()) # Printing values of the dictionary
# print(myDictionary.items()) # Printing keys and values together of the dictionary , gives a tuple

# updatedictionary= {
#     "friend": "a friend"
# }
# myDictionary.update(updatedictionary)
# myDictionary.update({"we" : "people"})
# print(myDictionary)
print(myDictionary.get("fast"))


