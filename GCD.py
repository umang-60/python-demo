#Program to find the GCD of two numbers
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))

if(num2==0):
    print(f"first number is GCD number:{num1}")
else:
    while num2!=0:
        rem=num1%num2
        num1=num2
        num2=rem
print(f"the GCD number is:{num1}")
