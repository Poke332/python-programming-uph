def watermelon(n):
    if n < 4:
        return "NO"
    else:
        for num1 in range(4, n+1):
            if num1 % 2 == 0:
                num2 = n - num1
                if num2 % 2 == 0:
                    return "YES"
    return "NO"

while True:
    user_input = input().strip()
    try:
        user_input = int(user_input)
        if 1 <= user_input <= 100:
            print(watermelon(user_input))
            break
        else:
            continue
    except:
        continue
    