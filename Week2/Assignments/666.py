user_input = input("Enter number: ").strip()

try:
    user_input = int(user_input)
except:
    print("Enter valid number")
    exit(code=401)

total = int()    
for i in range(1, user_input+1):
    six = int(("6"*i))
    total += six
print(total)