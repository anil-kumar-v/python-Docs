def factorial(n):
    fact=1
    for i in range(n,0,-1):
        fact=fact*i
    return fact

n=int(input("Enter the number:"))
res=factorial(n)
print("Factorial of a number is ",res)