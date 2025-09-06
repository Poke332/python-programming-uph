
def check_input_bool(input_msg: str):
  user_input = input(input_msg).strip().capitalize()
  
  if user_input == "True" or user_input == "Yes" or user_input =="Y":
    return True
  elif user_input == "False" or user_input =="No" or user_input =="N":
    return False
  else:
    print("Please input True/False or Yes/No, try again")
    exit()
