"""
    1. Ներածել (տրված է) միաչափ ցուցակ, տարրերի տիպը՝ ամբողջ թիվ, սահող կետով թիվ,
    տող: Հաշվել և արտածել միաչափ ցուցակի․
"""
from math import gcd

arr = ["15", "18", "a", "66", "9", "10.10", "50.2", "4.9", "ssabc", "af4444kd", "dfsjnf3333d", "asddf"]

int_digits = []
float_digits = []
str_el = []
for i in arr:
    try:
        int_digits.append(int(i))
    except ValueError:
        try:
            float_digits.append(float(i))
        except ValueError:
            str_el.append(i)


# 1.a ամբողջ թվերի ԱԸԲ-ը, իսկ սահող կետով թվերի միջին թվաբանականը
# print(f"gcd of integers: {gcd(*int_digits)} \navg of float numbers: {sum(float_digits) / len(float_digits)}")

# 1.b  պալինդրոմների քանակը
def is_palindrome(item):
    str(item)
    if len(item) > 1:
        return item == item[::-1]


count = 0
for i in arr:
    if is_palindrome(i):
        count += 1

# print(count)

# 1.c  երկնիշ և ոչ պարզ ամբողջ թվերի գումարը
digits = [*int_digits, *float_digits]
summer = 0
for i in digits:
    if len(str(i)) == 2:
        for j in range(2, i // 2):
            if i % j == 0:
                summer += i
                break
# print(summer)

# 1.d այն տողերի քանակը, որոնք բաղկացած են միայն տառերից կամ թվանշաններից
counter = len(digits)
for i in str_el:
    if i.isalpha():
        counter += 1
# print(counter)


# 1.e այն տողերի քանակը, որոնք սկսվում կամ ավարտվում են ‘abc’ ենթատողով
tox_counter = 0
for i in str_el:
    if i.startswith("abc") or i.endswith("abc"):
        tox_counter += 1
# print(tox_counter)


""""
    2. Ներածել (տրված է) սիմվոլային տող․
"""
tox = ["a1fs ", "   aFSAsaba451", "sdFFa   ", "a1abasFDfd", "SDFfsf"]

# 2.a տողից հեռացնել սկզբի և վերջի պրոբելները
stripted = [i.strip() for i in tox]
# print(stripted)

# 2.b տողում մեծատառերը փոխարինել համապատասխան փոքրատառերով, իսկ
# փոքրատառերը՝ համապատասխան մեծատառերով

swapcase_list = []
for i in tox:
    i = i.swapcase()
    swapcase_list.append(i)
# print(swapcase_list)

# 2.c տողից հեռացնել առաջին ‘a1’ ենթատողերը
for i in tox:
    if i.startswith("a1"):
        tox.remove(i)
# print(tox)

# 2.d տողում բոլոր ‘aba’ ենթատողերը փորարինել ‘*’ սիմվոլով
for i in range(len(tox)):
    if "aba" in tox[i]:
        tox[i] = tox[i].replace(tox[i], "*")
# print(tox)


"""
    3. Ներածել (տրված են) երկու տող՝ S1,S2
"""

S1 = "absd efg cbsde dd sadbsd adasdbsd ads"
S2 = "bsd"

# 3.a եթե S2-ը S1-ի ենթատողն է, ապա S1-ի մեջ S2-ի բոլոր հանդիպումներից առաջ և հետո
# ավելացնել ‘*’ սիմվոլը

# if S2 in S1:
#     S1 = S1.replace("bsd","*bsd")
# print(S1)

# 3.b եթե եթե S1-ի մեջ S2-ի հանդիպումների քանակը >3, ապա S1-ի մեջ S2-ի բոլոր
# հանդիպումները փոխարինել ‘0110’ ենթատողով

if S2 in S1 and S1.count(S2) > 3:
    S1 = S1.replace(S2, "0110")
# print(S1)

"""
    4. Ներածել (տրված են) երկու տող՝ S1,S2ֈ Ստանալ S3 տող, որը բաղկացած կլինի
"""

S1 = "qwertyuiop"
S2 = "asdfghuiop"

# 4.a S1 և S2 տողերի ընդհանուր բառերից
s1_letters = list(S1)
s2_letters = list(S2)
S3 = ""
for i in S1:
    if i in S2:
        S3 += i
# print(S3)

# 4.b S1 և S2 տողերի ոչ ընդհանուր բառերից այնպես, որ S3-ի սկզբում լինեն S1-ի
# բառերը, հետո S2-ի բառերը

s3 = ""
for i in s1_letters:
    if i not in S2:
        s3 += i
for j in s2_letters:
    if j not in S1:
        s3 += j
# print(s3)


"""
    5. Ներածել (տրված են) 2 բազմություն.
"""

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {5, 6, 7, 8}

# 5.a առաջին բազմությունից հեռացնել երկրորդ բազմության բոլոր տարրերը

# for i in set2:
#     set1.remove(i)
# print(set1)

# 5.b եթե երկրորդ բազմությունն առաջինի ենթաբազմությունն է, ապա ստեղծել նոր
# բազմություն առաջինի այն տարրերից, որոնք չեն մտնում երկրորդի մեջ

set3 = set()
if set2.issubset(set1):
    set3 = set1.difference(set2)
# print(set3)


"""
    6. Բառարանով ներածել ուսանողի հետևյալ տվյալները․ անուն, ազգանուն, խմբի համար, 
    լիկվիդ ունի, թե ոչ, 5 առարկաների գնահատականներ․
"""
# student = {}
# while True:
#     name = input("Enter name: ")
#     lastname = input("Enter lastname: ")
#     group_num = int(input("Enter the group number: "))
#     have_likvid = bool(int(input("if have likvid type 1, otherwise 0: ")))
#     marks = [int(input("Enter marks: ")) for i in range(5)]
#
#     student['name'] = name
#     student["lastname"] = lastname
#     student["group_num"] = group_num
#     student["have_likvid"] = have_likvid
#     student["marks"] = marks
#
#     break

# 6.a եթե ուսանողը լիկվիդ չունի և գնահատականների միջին թվաբանականը >10, ապա
# ավելացնել նոր տվյալ՝ թոշակ, 5000 արժեքով
# student_marks = student.get("marks")
# avg = sum(student_marks) / len(student_marks)
# if student.get("have_likvid") is False and avg > 10:
#     student["pension"] = 5000
# print(student)


"""
    7. Ներածել ուսանողների խմբի տվյալներ բառարաններից բաղկացած ցուցակի տեսքով, 
    որտեղ ամեն ուսանողի համար տրվում են հետևյալ տվյալները․ անուն, ազգանուն, խմբի
    համար, 5 առարկաների գնահատականներ․
"""
all_students = []
while True:
    current_student = {}
    name = input("Enter name: ")
    lastname = input("Enter lastname: ")
    group_num = input("Enter the group number: ")
    marks = [int(input("Enter marks: ")) for i in range(5)]

    current_student['name'] = name
    current_student["lastname"] = lastname
    current_student["group_num"] = group_num
    current_student["marks"] = marks

    all_students.append(current_student)

    end_loop = int(input("Exit? Yes-1, No-0: "))
    if end_loop:
        break


# 7.a ամեն ուսանողի համար ավելացնել նոր դաշտ՝ լիկվիդ yes կամ no արժեքով,
# կախված տվյալ ուսանողի որևէ առարկայից լիկվիդ ունենալուց

for i in range(len(all_students)):
    std_mark = all_students[i].get("marks")
    for j in std_mark:
        if 0 <= j < 8:
            all_students[i]["likvid"] = "yes"
            break
        elif 8 <= j <= 20:
            all_students[i]["likvid"] = "no"

# print(all_students)

# 7.b առանձնացնել ենթացուցակ 001 խմբի այն ուսանողներից, որոնց
# գնահատականները բարձր են 12-ից
student_sub_list = []
for i in range(len(all_students)):
    std_mark = all_students[i].get("marks")
    std_group = all_students[i].get("group_num")

    if std_group == "001":
        flag = True
        for j in std_mark:
            if j <= 12:
                flag = False
                break
        if flag:
            student_sub_list.append(all_students[i])
print(student_sub_list)
