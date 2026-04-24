'''
slice :
'''
#    0 1  2   3   4     5    6 7 8   9        10   +
l = [1,2,1.1,2.2,"tops",True,1,2,10,"python",False]
#    1 0  9   8   7     6    5 4 3   2        1    -                        

#start end
#print(l[0:6])

#print(l[-6:-1])
#print(l[-6:0:-1])

print(l[0])
print(l[6])

#start and end
print(l[0:4])
print(l[3:9])

#end
print(l[:7])
#start 
print(l[5:])

#start,end,jump
print(l[0:8:3])
print(l[0:10:4])


#start
print(l[-6:-1])
print(l[-10:-3])

#negtive
print(l[-11:-1:3])

#string revser
print(l[::-1])
