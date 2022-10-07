all_student = []

while True:
    mylist = []
    username = input("Enter username: ")
    lastname = input("Enter lastname: ")
    age = int(input("Enter age: "))
    is_likvid = bool(int(input("If student is likvid type 1, if not type 0: ")))
    mylist.append(username)
    mylist.append(lastname)
    mylist.append(age)
    mylist.append(is_likvid)
    all_student.append(tuple(mylist))

    end_loop = bool(int(input("End the loop(YES`1, NO`0): ")))
    if end_loop:
        break

    print("- - - - - - - - - - - - - - - - - - - - -")


def remuveDuplicate(array):
    arr = []
    for i in range(len(array)):
        if array[i] not in arr:
            arr.append(array[i])

    return arr


arr = remuveDuplicate(all_student)
print(arr)
