#check for the prime number
num=int(input("enter the number:"))
flag=False
for i in range(2,num):
    if num%i==0:
        flag=True
        break
if(flag==True):
    print("this is not prime")
else:
    print("this is prime")
