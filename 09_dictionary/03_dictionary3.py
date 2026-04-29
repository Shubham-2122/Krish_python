'''
    value match store
'''

d1 = {"A":100,"B":200,"C":300}
d2 = {"A":100,"B":300,"A":400,"D":400,"E":500,"F":600}

d3 = {}

for i in d1:
    if i in d2:
        d3[i] = d1[i]

print(d3)
