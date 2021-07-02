story= "once upon a time there was Vidhi Sharma studying the basics of chemistry, and she loved it! "
# String functions-----

# 1. Know the length of your variable. 'len' returns the length of char.
print(len(story))

# 2. string.endswith tells whether the string ends with a certain thing or not... and gives result in boolean, ie. true or false
print(story.endswith("hahudbiuadn"))
print(story.endswith("loved it! "))

# 3. string.count counts the no. of certain characters
print(story.count("o"))

# 4. string.capitalize capitalises 1st letter of string
print(story.capitalize())

# 5. string.find finds a word, returns index of 1st occurance
print(story.find("loved"))
print(story.find("lovd")) # -1 = not there

#  6. replace- replaces.. all occurances
print(story.replace("loved" , "was thrilled by studying "))