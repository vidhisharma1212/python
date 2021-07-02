fname = input("Enter file name: ")
try: 
    if len(fname) < 1:
        fname = "mbox-short.txt"
    fh = open(fname)
except:
    print('File not found:',fname)
    quit()
count = 0
for line in fh:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    l= line.split()
    print(l[1])
    count=count+1
print("There were", count, "lines in the file with From as the first word")