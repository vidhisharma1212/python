with open('donkey.txt') as f:
    x= f.read()

x= x.replace('donkey', '######')
# x= x.replace('Donkey', '######')

with open('donkey.txt', 'w') as f:
    f.write(x)

