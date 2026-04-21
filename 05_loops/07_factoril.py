'''
5! = 5*4*3*2*1 = 120
4! = 4*3*2*1 = 24

'''

num = int(input("Enter your num :"))
fact = 1

for i in range(1,num+1):
    fact *= i

print("factorial : ",fact)
