'''
list ,tuple,distionary

list [] : slice
tuple () : Slice, 
  {
      key : value,
      key : value
  }
'''

t = (1,2,1,3,4,5,"shubham")

print(t)
#print(t.index(2))
print(t.count(1))
    
l = [1,2,3,4,"Tops","krish","shubham",5,6,"python",True,True,False,8,9]
t1 = (1,2,"Tops",3,4,"krish",True,"shubham",5,"python",6,True,False,8,9)


print(l)
l.append(10)
print(l)

l.pop()
l.pop()
print(l)

print(l.count(1))

#value
l.remove("Tops")
print(l)

l.pop(1)
print(l)

print(l)
l1 = [100,200,300]

print(l1)

l.extend(l1)
print(l)

l.reverse()
print(l)

data = [2,3,4,5,10,2,1]
print(data)
print(max(data))
print(min(data))
print(sum(data))

data[3] = "sujal"
print(data)


