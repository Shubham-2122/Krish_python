'''

File : Enter log Day time ,Excel File Management
There are three oprations
W : write
R : Read
A : Append

text file

'''

# w : file created and file under print statement
file=open("test.txt","w")
file.write("This is File Mangement Write Data Mode Krisha panchal")
file.close()
print("Successfully Data written in File")
print("****************************************")

# R : File Under Data Show python terminal
file=open("test.txt","r")
print(file.read())
print("****************************************")

#A : append Data Add Old File New Entery
file =open("test.txt","a")
file.write("\nShubham jadav")
file.write("\nSujal jadav")
file.close()
print("File Appended Successfully")
print("****************************************")


# W+ , R+

file=open("demo.txt","w+")
file.write("This is File new written W+ mode.")
print("current File Position : ",file.tell())
#seek position change in text file
file.seek(0)
print(file.read())
file.close()
print("***************************************")

























