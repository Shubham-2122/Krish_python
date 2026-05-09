'''
    finally : block of code whenre use to excpetion
    error or yes or not
    finally allow


    
'''


try:
    print("start code")
    a = int(input("Ennter your A :"))
    b = int(input("Ennter your B :"))
    c = a/b
    print("Division :",c)
    l = [1,2,3,4,5]
    index = int(input("Enter your index :"))
    print(l[index])
except Exception as d:
    print("caught error:",d)
finally :
    print("final data")
    
print("End Code")
