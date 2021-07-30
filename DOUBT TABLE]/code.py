# def table(number):
#     for i in range(1,11):
#         print(f"{number}X{i}={number * i}")
#         # return(number,'X',i,'=',number * i)

# # table(5)
# for numbers in range (2,21) :
#     with open(f"table{numbers}.txt", "w") as f :
#         f.write(f"{numbers}X{i}={numbers * i}")

for i in range(2,21):
    with open (f"this_of_{i}.txt", 'w')as f :
        for j in range(1,11):
            f.write(f"{j}X{i}={j * i}\n")