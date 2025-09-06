pi = 3.1415926
while True:
  radius = input("Input Radius of a Circle: ")

  try:
    radius = float(radius)
    area = pi*radius**2
    print(f'The area of a cirle with radius of {radius} is {area}')
  except:
    print("Radius input not a number")
    continue
  
  break