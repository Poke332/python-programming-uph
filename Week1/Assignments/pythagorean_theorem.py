opposite = input("Input the length of the opposite side of a right sided triangle: ")
adjacent = input("Input the length of the adjacent side of a right sided triangle: ")

try:
  opposite = float(opposite)
  adjacent = float(adjacent)
except:
  print("Invalid number inputted to one of the sides, try again")
  exit()
  
hypotenuse = (opposite**2 + adjacent**2)**0.5

print(f'The hypotenuse length of said right sided triangle is {hypotenuse:.2f}')