print ("Armstrong")
n=input("Enter number")
s=0
new=n
while(n>=1):
    r=n%10
    s=s+(r**3)
    n=n/10
if (s==n):
    print ("It is an armstrong number")
else:
    print ("It is not an armstrong number")

