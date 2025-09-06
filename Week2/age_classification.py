user_age = input("What is your age? ").strip()

try:
    user_age = int(user_age)
    
    if 0 <= user_age <= 12:
        print("User is a child")
    elif 13 <= user_age <= 19:
        print("User is a teen")
    elif 20 <= user_age <= 64:
        print("User is an adult")
    elif user_age >= 65:
        print("User is a senior")
    else:
        print("User age must not be negative")
except:
    print("Please enter valid number")