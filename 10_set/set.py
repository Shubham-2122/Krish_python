'''
    set : A set is collection of unquie value
    mutable : {we can chnage data}

'''
# duplicate value not store
s = {1,2,3,4,4,5}

print(s)

s.add(6)
print(s)

#value update
s.update([2,7])
print(s)

s.remove(7)
print(s)

s.discard(5)
print(s)

s.pop()
s.pop()
print(s)

