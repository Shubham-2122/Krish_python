'''
    function : it's block of code.when we need when use it
            : call it
            ()
            1) predefiend function : libray function
                li.pop()
            2) user defiend function : user created
                catgory :
                    1) without argument & without return
                    2) with argument & without return
                    3) with arhumne & with return value
    def user-name():
        code
    user-name()
    user-name()
'''

# without argument & without return
def printLine():
    print("*"*40)

printLine()
print("Hello krisha panchal")
printLine()

def add():
    a = 30
    b = 10
    print("Sum : ",a+b)

add()
printLine()
add()


# with argument & without return

def sum(x,y):
    print("SumD : ",x+y)

printLine()
sum(35,20)
printLine()
sum(67,35)

# with argument & with return

def sub(a,b):
    return a-b

printLine()
result = sub(40,15)
print("sub :",result)
printLine()
print("sub :",sub(50,12))
printLine()







