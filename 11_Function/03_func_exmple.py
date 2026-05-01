def demo(a,b,c,*d):
    print("A :",a," B : ",b," C :",c," D: ",d)

demo(1,2,3,4,5,6,7,8,9)

def demo2(a,b,c,*d,**e):
    print("A :",a," B : ",b," C :",c," D: ",d," E :",e)

demo2(1,2,3,4,5,6,7,8,x=10,y=20,z=30,n=40)
