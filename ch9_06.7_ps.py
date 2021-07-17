with open('ch9_06_7_pssample.txt') as f:
    content= f.read()
# .lower()
if 'python' in content:
    print('present')
else:
    print('not present')