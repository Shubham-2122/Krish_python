import random

file =open("data.txt","w")
for i in range(1,11):
    file.write(str(random.randint(1,50))+",")
file.close()

file=open("data.txt","r")
even=open("even.txt","w")
odd =open("odd.txt","w")

#print(file.read())
l = file.read().split(",")[:-1]
print(l)

for i in l:
    if int(i)%2 ==0:
        even.write(i+",")
    else:
        odd.write(i+",")
        
file.close()
even.close()
odd.close()

#read
print("Data File Content")
file = open("data.txt","r")
print(file.read())
file.close()

print("Even File Content")
even = open("even.txt","r")
print(even.read())
even.close()

print("Odd File Content")
odd = open("odd.txt","r")
print(odd.read())
odd.close()






















