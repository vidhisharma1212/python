fname = input("Enter file name: ")
try: 
    fh = open(fname)
except:
    print('File not found:',fname)
    quit()
lst = list()
for line in fh:
    a=line.rstrip()
    a=line.split()
    for word in a:
        if word in lst:
            continue
        else:
            lst.append(word)
print(lst.sort())
