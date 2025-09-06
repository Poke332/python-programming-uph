P = 1
n = input("How many times are the interest compounded? ")

try:
  n = float(n)
except:
  print("Invalid number inputted, try again")
  exit()
  
future_value = P * (1 + 1/n)**(n)

print(f'Raymond\'s money at the end of 2025 is {future_value:.3f}$')

# Conclusion: As value of n gets larger, the rate of which the compounded money increases gets smaller and smaller until its increasing rate is negligible
