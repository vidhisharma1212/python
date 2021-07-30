with open('donkey.txt') as f:
    x= f.read()

x= x.replace('donkey', '######')
# x= x.replace('Donkey', '######')

with open('donkey.txt', 'w') as f:
    f.write(x)

'''My code which was tried by me-'''

# with open('donkey.txt', 'r') as f: 
#     x= f.read()
#     if 'donkey' in x:
#         y=True
#     elif 'Donkey' in x:
#         y= True
#     else:
#         y=False
    
#     if y==True:
#         f.write('######') 
#         #f.write('Donkey')= '######'        