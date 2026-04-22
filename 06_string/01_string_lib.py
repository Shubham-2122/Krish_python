'''
string : group of char

'''

s = "krish Panchal"
p = "HELLO PYTHON"

print(s)

#string length
print(len(s))

#string lib function
print(s.capitalize())
print(s.casefold())
print(s.upper())
print(p)
print(p.lower())

# capital and small
print(s.swapcase())

#word cpital letter
print("python programming".title())

#total char inside center
print(s.center(30,"*"))
print(s.center(30,"-"))

# char find
print(s.count("h"))

#last string check true/false
print(s.endswith("hal"))

#start with index 
print(s.find("Pan"))

#start index
print(s.index("k"))
print(s.index("c"))

#print(p.index("L",2))

#only alphabetate
print("tops".isalpha())
print("123".isnumeric())

#replce
print("hello".replace("l","w"))






