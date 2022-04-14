t=eval(input("Enter tuple of numbers:"))
l=len(t)
sum=0
for i in t:
    sum=sum+i
print("The sum=",sum)
print("The average=",sum/l)