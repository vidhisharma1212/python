text = "X-DSPAM-Confidence:    0.8475"
a= text.find('    ')
b= text.find('5')+1
g= text[a+4:b]
f= float(g)
print(f)