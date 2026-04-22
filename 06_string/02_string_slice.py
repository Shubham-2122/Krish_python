'''
string slice
string start index 0

'''
#   01234567890123456  +
s ="Tops Technologies"
#   76543210987654321  - 

#single letter index number
print(s[0])
print(s[6])

#start and end
print(s[0:4])
print(s[3:13])

#end
print(s[:7])
#start 
print(s[5:])

#start,end,jump
print(s[0:15:3])
print(s[0:16:4])


#start
print(s[-6:-1])
print(s[-17:-13])

#negtive
print(s[-17:-1:3])

#string revser
print(s[::-1])
