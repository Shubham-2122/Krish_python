'''
a b c

if codi:
    if codi:
        print()
    else:
        print()
else:
    print()

20 10 30

'''


a = int(input("Enter your A :"))
b = int(input("Enter your B :"))
c = int(input("Enter your C :"))

if a > b:
    if a > c:
        print("A max")
    else:
        print("C max")
elif b > c:
    print("B max")
else:
    print("C max")
