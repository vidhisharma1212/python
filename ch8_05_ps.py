def stars(n):
    for i in range(n): # (answered below )why here not (n+1) as it can go only up to (n-1)th value?
        print("*" * (n-i))
        # 1 (i=0)--> (3-0) times * [3]
        # 1 (i=1)--> (3-1) times * [2]
        # 1 (i=2)--> (3-2) times * [1]

j=int(input("Enter no. of stars : \n"))
print(stars(j))
