num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

try:
    num1 = float(num1)
    num2 = float(num2)
    num3 = float(num3)
except:
    print("One of the number inputs are invalid, try again")
    exit()
    
num_list = [num1, num2, num3]
current_largest = 0

for i in range(len(num_list)):    
    if num_list[i] > current_largest:
        current_largest = num_list[i]

print(f"Largest number is {current_largest}")