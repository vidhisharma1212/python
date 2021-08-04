f=open('contenth.txt')
content= f.readline().lower()
for line in content:
    if 'python' in line:
        print('line is: ',line)
    else:
        print('not present')
f.close()