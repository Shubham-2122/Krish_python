def test(a=10,b=50,c=70,d=60):
    print("A :",a," B : ",b," C :",c," D: ",d)

#value pass
test(10,20,30,40)

#default fix 
test(10,20,30)
test(10,20,30,40)

test(10)

#b and c
test(b=20,c=89)

def info(name="Guest"):
    print("Name :",name)

info("krisha")
info()
info("Shubham")
