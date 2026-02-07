#Program to find the second largest array element.
lst=[3,5,7,1,4,9,5]
max=-1
secondmax=-1
for i in range(0,len(lst)):
    if(lst[i]>max):
        secondmax=max
        max=lst[i]
    elif(lst[i]>secondmax and secondmax!=max):
        secondmax=lst[i]

print(max)
print(secondmax)