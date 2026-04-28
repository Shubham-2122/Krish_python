'''
    1 : 1
    2 : 16
    3 : 27
    4 : 64
    5 : 125
    6 : 216
'''

d = {}
n = int(input("Enter your num : "))

for i in range(1,n+1):
    d[i] = i*i

print(d)

#for i in d:
#    print(i,":",d[i])
