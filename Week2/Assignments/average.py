total = float()
count = 0

while True:
    user_input = input("Enter number: ").strip()
    try:
        user_input = float(user_input)
    except:
        print("Enter valid number")
        continue
    
    if user_input == -1:
        break

    count += 1
    total += user_input

print(f"{(total/count):.2f}")