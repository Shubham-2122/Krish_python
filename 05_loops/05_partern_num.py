'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

1
2 3
4 5 6
7 8 9 10

'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

num = 1
n = 5

for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num += 1
    print()





