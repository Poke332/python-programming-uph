first_name = input("Enter Your First Name: ")
last_name = input("Enter Your Last Name: ")
nickname = input("Enter Your Nickname: ")
birth_year = input("Enter Your Birth Year: ")

try:
  birth_year = int(birth_year)
except:
  print("Invalid Number for Birth Year, try again")
  exit()

print(f'Hello, my name is {first_name} {last_name}. You can call me {nickname}. Im {2025 - birth_year} years old. Nice to meet you!')
