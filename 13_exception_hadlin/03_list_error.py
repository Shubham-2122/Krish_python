try:
    print("start code")
    a = int(input("Ennter your A :"))
    b = int(input("Ennter your B :"))
    c = a/b
    print("Division :",c)
    l = [1,2,3,4,5]
    index = int(input("Enter your index :"))
    print(l[index])
except IndexError as e:
    print("error caught :",e)
    
except ValueError as e:
    print("error caught :",e)
    
except ZeroDivisionError as e:
    print("error caught :",e)
    
print("End Code")
