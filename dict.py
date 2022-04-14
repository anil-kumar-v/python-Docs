rec={}
n=int(input("Enter no of sudents:"))
i=1
while i<=n:
    name=input("Enter name of the student:")
    marks=input("Enter the marks of the student:")
    rec[name]=marks
    i+=1
print("Name of the student","\t","Marks of the student")
for x in rec:
    print("\t",x,"\t\t",rec[x])