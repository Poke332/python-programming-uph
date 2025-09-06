num1 = input("Enter first number: ").strip()
num2 = input("Enter second number: ").strip()

try:
    num1 = int(num1)
    num2 = int(num2)
except:
    print("Enter valid number")
    exit()

if num1 > num2:
    num1, num2 = num2, num1
    
total = int()
for i in range(num1, num2+1):
    total += i
print(total)