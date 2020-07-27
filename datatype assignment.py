name = []
while len(name) < 10:
    if len(name) == 0:
        stud1 = input("enter name:")
        name.append(stud1)
        print(name)
        continue
    else:
        stud1 = input("enter name:")
        if stud1 in name:
            print("name already exist")
            continue
        else:
            name.append(stud1)
            print(name)

