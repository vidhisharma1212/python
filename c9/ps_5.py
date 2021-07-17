# from os import replace
list=['donkey','time','thinking','knows']


with open('donkey.txt') as f:
    x= f.read()


for word in list:
    x= x.replace(word, "#####")
    with open('donkey.txt', 'w') as f:
        f.write(x)
# with open('donkey.txt', 'w') as f:
    # for line in x:
        # for i in range(1,5):
            # if list[i] in line:
                # x= x.replace(list[i], "#####")
    # f.write(x)