def social_network_friend_matcher(name_input: str, f_path: str):
    try:
        name_1, name_2 = name_input.split()
    except:
        raise ValueError("Failed to split inputs, expected 2 names split by space")
    
    mutual_dict = dict()
    with open(f_path, "r") as f:
        for line in f:
            name, mutuals = line.strip().split(":")
            mutuals = mutuals.split(",")
            mutual_dict[name] = mutuals
    
    result = list()
    mutual_1, mutual_2 = mutual_dict.get(name_1, []), mutual_dict.get(name_2, [])
    
    if mutual_1 == []:
        return f"First name isnt registered in {f_path}"
    elif mutual_2 == []:
        return f"Second name isnt registered in {f_path}"
    
    for name in mutual_1:
        if name in mutual_2:
            result.append(name)
    
    if len(result) == 0:
        return "No Mutuals"
    return " ".join(result)


usr_input = input().strip()
print(social_network_friend_matcher(usr_input, "person.txt"))
