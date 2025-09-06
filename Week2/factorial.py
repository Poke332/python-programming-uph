def factorial(n):
    #factorial with function recursion
    if n == 0:
        return 1
    elif n < 0:
        return "factorial of a negatif number is undefined"
    else:
        return n*factorial(n-1)

n = input("Enter number: ").strip()

try:
    n = int(n)
    print(f"factorial of {n} with function: {factorial(n)}")
except:
    print("Enter valid number")
else:
    # factorial with for loop
    sum = 1
    for i in range(1, n+1):
        sum = sum*i
    print(f"factorial of {n} with for loop: {sum}")