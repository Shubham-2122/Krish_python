roll = int(input("Enter you roll no :"))
sname = input("Enter your name :")

s1 = int(input("Enter your subject 1 :"))
s2 = int(input("Enter your subject 2 :"))
s3 = int(input("Enter your subject 3 :"))

total = s1+s2+s3
per = total/3

print("Roll no :",roll)
print("Student Name :",sname)
print("total marks :",total)
print("percentage :",per)

if s1>40:
    if s2>40:
        if s3>40:
            if per >= 80:
                print("A grade Student")
            elif per >= 60:
                print("B grade Student")
            elif per >= 45:
                print("C grade Student")
            elif per >= 35:
                print("D grade Student")
            else:
                print("Fail student")
        else:
            print("s3 Student fail")
    else:
        print("s2 Student fail")
else:
    print("s1 Student fail")

    



