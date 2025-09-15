database = set()
user_input = str()

def registration_system(db, num=1):
    for _ in range(num):
        name = input().strip()
        if name not in db:
            db.add(name)
            print("OK")
        else:
            count = 1
            while True:
                new_name = name + str(count)
                if new_name not in database:
                    database.add(new_name)
                    print(new_name)
                    break
                count += 1
            

while True:
    user_input = input().strip()
    try:
        user_input = int(user_input)
        break
    except:
        continue

registration_system(database, user_input)
print(database)

