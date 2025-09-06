side = input("Enter length of side: ")

try:
    side = int(side)
except:
    print("Enter a valid integer")
else:
    for i in range(side):
        print("* "*side)