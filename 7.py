# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count=0
n=0
try:
    fh = open(fname)
except:
    print('File not found:',fname)
    quit()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line)
    count=count+1
    a= float(line[21:])
    n= n+a
avg= n/count
print("Average spam confidence:", avg)