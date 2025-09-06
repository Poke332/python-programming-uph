n = input("Enter number: ")

try:
    n = int(n)
except:
    print("Enter valid integer")
else:
    if 1 <= n <= 10:
        for i in range (1, n+1):
            print("*"*i)
    else:
        print("Enter number in range 1-10")