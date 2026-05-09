try:
    print("start code")
    a = int(input("Ennter your A :"))
    b = int(input("Ennter your B :"))
    c = a/b
    print("Division :",c)
#10.10 float value
except ValueError as e:
    print("error caught :",e)
    
# 10 / 0
except ZeroDivisionError as e:
    print("error caught :",e)
    
print("End Code")
