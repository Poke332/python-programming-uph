def registration_system(num):
    db = dict()
    output = []
    
    for _ in range(num):
        name = input().strip()
        if name not in db:
            db[name] = 0
            output.append("OK")
        else:
            db[name] += 1
            output.append(f"{name}{db[name]}")
            
    print("\n".join(output))
            

registration_system(int(input().strip()))

