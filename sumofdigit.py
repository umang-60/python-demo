#Program to find the sum of digits.
num=int(input("enter the number:"))
sum=0

while num > 0:
    digit=num%10 
    num//=10 
    sum=sum+digit    
print(sum)