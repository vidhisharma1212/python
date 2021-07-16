for i in range(2,20):
    f=open(f"multiplications_table_of_{i}", "w")
    for k in range(1,11):
            f.write(f"{i}X{k}={i*k}")
    break
f.close()