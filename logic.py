n=eval(input("Enter your list: "))
#n=[10,20,30,40]
n1=len(n)
mx=max(n[0],n[1])
smx=min(n[0],n[1])
for i in range(2,n1):
    if n[i]>mx:
        smx=mx
        mx=n[i]
    else:
        if n[i]>smx and mx != n[i]:
            smx=n[i]

print("The second largest number in the list is ",smx)





'''n=eval(input("Enter your list:"))
#n=[10,20,30,40]
n1=len(n)
mx=max(n[0],n[1])
mx_1=min(n[0],n[1])

for i in range(2,n):
    if n[i]>mx:
        mx_1=mx
        mx=n[i]
    else:
        if n[i]>mx_1 and mx!=n[i]:
         mx_1=n[i]

print("Second highest number in the list is : ",mx_1)'''