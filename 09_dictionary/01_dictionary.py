'''
    dictionary : key and value pair
               : key always unique
               : as object use { key : value}
'''

d = {101:"shubham",102:"krisha",103:"het",104:"varj",105:"manthan",106:"piyush",107:"shubham"}

print(d)

#update key
d[103] = "shlok"

print(d)

#get key find value
print(d.get(105))

# pop key remove element
d.pop(106)
print(d)

#items will convert data
print(d.items())

#keys
print(d.keys())

#value
print(d.values())

print(d)

# new change last popitem
d.popitem()
print(d)

d1 = {109:"henil",110:"harshil",111:"priya"}

d.update(d1)
print(d)

for i in d:
    print(i," : ",d[i])

