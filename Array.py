import array
from array import *
arr=array('i',[])
n=int(input("Enter the length of the array: "))

for i in range(n):
    x=int(input("Enter the  next number: "))
    arr.append(x)

print(arr)


val=int(input("Enter the value to search:"))

k=0
for j in arr:
    if j==val:
        #print(k)
        break
    k+=1
print(arr.index(val))


 