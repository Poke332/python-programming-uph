from useful_modules import check_input_bool

print("Can we go outside today?")

is_weekend = check_input_bool("Is it a weekend? ")
is_raining = check_input_bool("Is it raining? ")
is_sunny = check_input_bool("Is it sunny? ")
is_holiday = check_input_bool("Is it a holiday? ")

if is_raining:
  print("We're not going outside")
elif (is_weekend or is_sunny or is_holiday) and not is_raining:
  print("Yes, we can go outside")
else:
  print("Error, edge case detected")