first_name = input("What is your first name? ").strip().capitalize()
last_name = input("What is your last name? ").strip().capitalize()
full_name = " ".join([first_name, last_name])

print(f"Welcome {full_name}!")
