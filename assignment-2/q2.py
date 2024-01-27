n=int(input("Enter a number:"))

factorial = 1
if n < 0:
    print("factorial is not exist for negative numbers")
elif n == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,n+1):
        factorial=factorial*1
    print("the factorial of",n,"is",factorial)    
