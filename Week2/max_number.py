largest = int()

while True:
    number = input("Enter number: ")
    try:
        number = int(number)
    except:
        print("Enter valid number")
        continue
    
    if number > largest:
        largest = number
    
    if number == -1:
        break

print(largest)