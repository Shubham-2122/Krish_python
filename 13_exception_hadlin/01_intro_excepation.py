'''
excpetion : logic error ,data invalid
hadling : error handle

program : run code line by line end output
'''

try:
    print("start code")
    a = int(input("Ennter your A :"))
    b = int(input("Ennter your B :"))
    c = a/b
    print("Division :",c)
except :
    print("error caught")
print("End Code")
