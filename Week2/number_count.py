N = input("Enter number: ")
try:
    N = int(N)
except: 
    print("Enter valid integer")
else:
    for num in range(1, N+1):
        print(num, end=" ")
    print()