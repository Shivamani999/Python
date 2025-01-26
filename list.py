# syntax [] or list()
# can use anytype of datatypes in a list
# this will be in a specified order
# list is mutable
import random

empty_lst = []
empty_lst1 = list()

num = [1,2,10,3,4,29,5,6,12]
# print(num)
# print(num[0])
# print(num[1])
# print(num[-3])

# print(num[0:])
# print(num[:6])
# print(num[::2])
#
# print(len(num))
#
# print(19 in num)
# print(num[5] in num)
#
# num.append(10)
# print(num)
# num.insert(3,30)
# print(num)
# num.remove(30) # uses value
# print(num)
# num.pop(3) # uses index
# print(num)
# # del num
# # print(num)
# num.clear()
# print(num)
#
# num1 = [7,8,9,10,11,12]
# num = num1.copy()
# print(num)
#
# num.extend(num1)
# print(num)
#
# num.sort()
# print(num)
#
# print(num.count(10))
#
# print(num.index(10))
#
# num.reverse()
# print(num)

# for i in num:
#     print(i, end="")
#
# for i in num:
#     if i % 2 == 0:
#         print(i)

# num.reverse()
# for i in num:
#     print(i, end="")

# print(max(num))
# print(min(num))
#
# max = 0
# for i in num:
#     if i > max:
#         max = i
# print(max)

# max_sec = 0
# max = 0
# for i in num:
#     if i > max:
#         max = i
# for i in num:
#     if i > max_sec and i != max :
#         max_sec = i
# print(max_sec)

# num.sort()
# print(num[len(num)-1])
# print(num[0])
# print(num[len(num)-2])

# num[:0]=[6]
# print(num)
#
# print(random.choice(num))

max_index, max, min_index = 0, 0, 0
min = float("inf")
for i in num:
    if i > max:
        max = i
for i in num:
    if i < min:
        min = i

print(num.index(max))
print(num.index(min))