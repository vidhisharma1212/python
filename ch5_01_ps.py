translationdictionary= {
    "Moorti" : "Statue",
    "Kursi" : "Chair",
    "Kitab" : "Book",
}

print("You can know the meaning of any word from the following ,", translationdictionary.keys())
a= input("Enter the word you want to translate in english : \n")
# print("The word you searched for, has a meaning,", translationdictionary[a]) # May throw an error 
print("The word you searched for, has a meaning,", translationdictionary.get(a))