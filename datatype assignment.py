#date = 25-7-2020
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


#data = 27-7-2020

#counting names from list

list1 = ["chaitanya","chaitanya","priya","chaitanya","rita","chaitanya","rita","chaitanya","priya","priya","rita"]
name_count1 = list1.count("chaitanya")
name_count2 = list1.count("priya")
name_count3 = list1.count("rita")
print("the count of name:chaitanya is",name_count1)
print("the count of name:priya is",name_count2)
print("the count of name:rita is",name_count3)



names = ['aman','preet','singh']
id = [147,258,369]
amount = [1400,2000,6500]
n = int(input("please enter id:"))
number = id.index(n)
print(amount[number])




