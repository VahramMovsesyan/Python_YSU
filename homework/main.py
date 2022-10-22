"""
    1. Ներածել (տրված է) միաչափ ցուցակ, տարրերի տիպը՝ ամբողջ թիվ, սահող կետով թիվ,
    տող: Հաշվել և արտածել միաչափ ցուցակի․
"""
from math import gcd

arr = ["15","18","a","66","9","10.10","50.2","4.9","ssabc","af4444kd","dfsjnf3333d", "asddf"]

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
print(f"gcd of integers: {gcd(*int_digits)} \navg of float numbers: {sum(float_digits) / len(float_digits)}")

# 1.b  պալինդրոմների քանակը
def is_palindrome(item):
    if len(item) > 1:
        return item == item[::-1]
count = 0
for i in arr:
    if is_palindrome(i):
        count += 1

print(count)

# 1.c  երկնիշ և ոչ պարզ ամբողջ թվերի գումարը
digits = [*int_digits,*float_digits]
summer = 0
for i in digits:
    if len(str(i)) == 2:
        for j in range(2, i//2):
            if i % j == 0:
                summer += i
                break
print(summer)

# 1.d այն տողերի քանակը, որոնք բաղկացած են միայն տառերից կամ թվանշաններից
counter = len(digits)
for i in str_el:
    if i.isalpha():
        counter += 1
print(counter)


# 1.e այն տողերի քանակը, որոնք սկսվում կամ ավարտվում են ‘abc’ ենթատողով
tox_counter = 0
for i in str_el:
    if i.startswith("abc") or i.endswith("abc"):
        tox_counter += 1
print(tox_counter)