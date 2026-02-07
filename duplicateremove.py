#remove duplicate element from the list
lst=[]
n=int(input("enter the size of list:"))
for i in range(1,n+1):
    x=int(input("enter the element:"))
    lst.append(x)

print(lst)
lst2=set(lst)
print(lst2)