import temp_convert as tmpc

user_input = input("Enter temperature degrees: ").strip()
try:
    user_input = float(user_input)
except ValueError:
    print("Error: Input valid number, try again")
    exit()

temp_type = input("Is it in celcius/fahrenheit?\n 1: Celcius\n 2: Fahrenheit\nYour choice (number)? ").strip()

print("="*30)
if temp_type == "1":
    print(f"{user_input} Celcius\nto\n{tmpc.celcius_to_fahrenheit(user_input):.2f} Fahrenheit")
elif temp_type == "2":
    print(f"{user_input} Fahrenheit\nto\n{tmpc.farenheit_to_celcius(user_input):.2f} Celcius")
else:
    print("Enter supported temps and try again")