# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File not found :',fname)
    quit()
for a in fh:
    a=a.upper()
    a=a.rstrip()
    print(a)