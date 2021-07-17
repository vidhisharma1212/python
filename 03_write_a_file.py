f= open('net.txt', 'w')
f.write("Please write this to the file")
f.close()

f= open('net.txt', 'a')
f.write("I am appending this file.")
f.close()