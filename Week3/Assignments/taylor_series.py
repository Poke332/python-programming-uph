def factorial(n):
    total = 1
    for i in range(2, n+1):
        total *= i
    return total

def taylor_series(n):
    total_sum = 0
    for i in range(n+1):
        current = 1
        if i > 0:
            current /= factorial(i)
        total_sum += current
    return total_sum


user_input = input().strip()
try:
    user_input = int(user_input)
except:
    print("Enter valid integer, try again")
    exit()

print(f'{taylor_series(user_input):.6f}')