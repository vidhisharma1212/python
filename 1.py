def computepay(h, r):
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate= input("Enter Rate:")
    r= float(rate)
    if h<=40:
        pay=h*r
    else:
        hn=h-40.0
        pay=(40.0*r+(hn*(r*1.5)))
    return pay

p = computepay(10, 20)
print("Pay", p)
