n=int(input("Enter number: "))
sum=0
if(n%2==0):
    for n in range(0,n+1,2):
        sum+=n
        print("Sum of even numbers is: ",sum)
else:
    for n in range(1,n+1,2):
        sum+=n
        print("Sum of odd numbers is: ",sum)