#   task 1
#
# arr = []
# while True:
#     inp = input("Enther item: ")
#
#     if inp == "0":
#         print(f"new list is: {arr}")
#         break
#     arr.append(inp)
#
# digits = []
# for i in arr:
#     try:
#         digits.append(int(i))
#     except ValueError:
#         try:
#             digits.append(float(i))
#         except ValueError:
#             continue
#
# min_index = digits.index(min(digits))
# max_index = digits.index(max(digits))
#
# sublist = digits[min_index : max_index + 1]
#
# summary = 0
# for i in sublist:
#     summary += i
# print(summary)


#    task 2
#
# arr = []
# while True:
#     inp = input("Enther item: ")
#
#     if inp == "0":
#         print(f"new list is: {arr}")
#         break
#     arr.append(inp)
#
# digits = []
# for i in arr:
#     try:
#         digits.append(int(i))
#     except ValueError:
#         try:
#             digits.append(float(i))
#         except ValueError:
#             continue
#
#
# def is_palindrome(item):
#     return item == item[::-1]
#
#
# palindrome_count = 0
# for i in digits:
#     if is_palindrome(str(i)):
#         palindrome_count += 1
#
# print(f"All digits from list: {digits}")
# print(f"Count of palindrome numbers {palindrome_count}")

#   task 3
#
# arr = []
# while True:
#     inp = input("Enther item: ")
#
#     if inp == "0":
#         print(f"new list is: {arr}")
#         break
#     arr.append(inp)
#
# digits = []
# for i in arr:
#     try:
#         digits.append(int(i))
#     except ValueError:
#         try:
#             digits.append(float(i))
#         except ValueError:
#             continue
#
# print(digits)
# for i in range(len(digits)):
#     min_val = min(digits)
#     max_val = max(digits)
#
#     if digits[i] == min(digits) and digits[-i - 1] == max(digits):
#         digits[i] = max_val
#         digits[-i - 1] = min_val
#
#     if digits[i] == max(digits) and digits[-i - 1] == min(digits):
#         digits[i] = min_val
#         digits[-i - 1] = max_val
#
# print(digits)


#   task 5
#
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
#
# set(str1)
# set(str2)
# array = set()
# for i in str1:
#     if i in str2:
#         array.add(i)
#
# string = ''
# for i in array:
#     string += i
# print(string)


#       task 6
#
# x = list(input("Enther first string: "))
# y = list(input("Enther second string: "))
#
# arr = []
#
# for i in x:
#     if i not in y:
#         arr.append(i)
#
# for j in y:
#     if j not in x:
#         arr.append(j)
# string = ''
# for k in arr:
#     string += k
# print(string)
