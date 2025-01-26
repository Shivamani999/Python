# syntax () or tuple()
# can use anytype of datatypes in a tuple
# this will be in a specified order
# tuple is immutable


# empty_tuple = tuple()
# tuple_emp = ()
#
# tup = (1,2,3,6,6,6,6,4,5)
# lst = [1,2,3,4,5]
#
# print(type(tup))
# print(type(lst))
#
# print(len(tup))
# print(tup[0])
# print(tup[-3])
#
# print(tup[1:3])
#
# lst_tup=list(tup)
# print(type(lst_tup))
#
# tup_lst=tuple(lst_tup)
# print(type(tup_lst))
#
# print(tup.index(5))
# print(tup.count(6))

sample = [(10,20,40),(40,50,60),(70,80,90)]
#for t in sample:
    # print(t[:-1]+(100,), end=",")
    # lst = list(t)
    # lst[2] = 100
    # print(tuple(lst), end=" ")
    # comprehension of list: [exp for x in range/list/tuple/ if conditoin]
print([t[:-1]+(100,) for t in sample if t[0]>30])
