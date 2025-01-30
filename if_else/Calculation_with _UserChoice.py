n1=int(input("Enter number: "))
n2=int(input("Enter number: "))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
ch=int(input("Enter Your Choice: "))
if ch==1:
    print("Addition is: ",n1+n2)
elif ch==2:
    print("Subtraction is: ",n1-n2)
elif ch==3:
    print("Multiplication is: ",n1*n2)
elif ch==4:
    print("Division is: ",n1/n2)
else:
    print("Invalid Choice")
    