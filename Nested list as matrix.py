n=[[10,20,30,40],[50,60,70],[80,90]]
print(n)
print("Elements in Row wise:")
for r in n:
    print(r)
print("Elements in column wise:")
for i in range(len(n)):
    for j in range(len(n[i])):

        print(n[i][j],end=" ")
    print()