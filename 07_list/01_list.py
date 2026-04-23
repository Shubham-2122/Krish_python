'''
    list : group of defferent type value
    int,float,string,boolen
    list index start 0
    [] : add,remove,update
'''
    
l = [1,2,1.1,2.2,"tops",True,1,2,10,"python",False]

print(l)
print(len(l))

#list add only element
l.append(100)
print(l)

#list clear
#l.clear()
#print(l)

#copy list new list
l1 = l.copy()
#print(l)
print(l1)
l1.append(200)
print(l1)
print(l)

# l2 update and old l update
l2 = l
print(l)
print(l2)
l2.append(300)
print(l2)
print(l)

# indualy after remove
l.pop()
l.pop()
print(l)

#count
print(l.count(1))

# multiple element add
l3 = [1000,2000,3000]
print(l3)
l.extend(l3)
print(l)

#index find

print(l.index(10))
print(l.index("python"))

#insernt
l.insert(5,101)
print(l)

#pop index number delete
l.pop(10)
print(l)

#remove value
l.remove(10)
print(l)

#l.reverse()
print(l)

#list
for i in l:
    print(i)
    
#check true or false
print(102 in l)
