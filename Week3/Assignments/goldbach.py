def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    
    for num in range(2, n-1):
        if (n % num) == 0:
            return False
    else:
        return True
        
def goldbach_conjecture(even_number: int):
    for first_number in range(even_number):
        if is_prime(first_number):
            second_number = even_number - first_number
            if is_prime(second_number) and first_number + second_number == even_number:
                print(first_number, second_number)
                return [first_number, second_number]
    print("Not Found")

user_input = -1

while user_input % 2 != 0:
    user_input = input().strip()
    try:
        user_input = int(user_input)
    except:
        print("Enter valid number")
        continue
    
    if user_input % 2 != 0:
        print("Enter even number")


goldbach_conjecture(user_input)

