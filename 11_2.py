name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts= dict()
lst= list()

for line in handle:
    if line.startswith('From '):
        h= line.split()
        hr=h[5].split(":")
        counts[hr[0]]=counts.get(hr[0],0)+1

for k,v in counts.items():
    a=k,v
    lst.append(a)
lst.sort()
for hr,counts in lst:
    print(hr,counts)
