'''
    5 =  5+4+3+2+1+0 = 15
    10 = 10+9+8+7+6+5+4+3+3+2+1+0
    
'''

num = int(input("Enter your number :"))

def total(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

print("number of value : ",num)
print("num of total Sum :",total(num))

