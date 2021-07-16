# detecting spaces(double)
story2 = "once upon a time there was Vidhi Sharma  studying the basics of chemistry, and she loved it! "
print(story2.find("  "))

storyy= "hello  there    people!"

# Find double spaces from storyy
doublespaced= storyy.find("  ")
print(doublespaced) 

# ques. 4 Replace the double space--
replacedoublespace= storyy.replace("  ", " ")
print(replacedoublespace)