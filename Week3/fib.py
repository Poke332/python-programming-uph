def fibonaci(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonaci(n-2) + fibonaci(n-1)

user_input = input("Enter number: ")

try:
    user_input = int(user_input)
    print(fibonaci(user_input))
except:
    print("User input must be valid number")