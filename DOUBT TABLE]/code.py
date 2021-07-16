def table(number):
    for i in range(1,11):
        # return(f"{number}X{i}={number * i}")
        return(number,'X',i,'=',number * i)

for numbers in range (2,21) :
    f= open(f"table{numbers}.txt", "w")
    f.write(str(table(numbers)))

f.close()