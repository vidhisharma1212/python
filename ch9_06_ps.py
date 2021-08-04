with open('content.txt') as f:
    content= f.read().lower()
    m= content.replace('python','#####')

if 'python' in content:
    n=open('content.txt','w') 
    n.write(m)
    print('present')
    n.close()
else:
    print('not present')