# syntax {} or set()
# can use anytype of datatypes in a list
# this will be in a unspecified order
# set is immutable
# it won't accept the duplicates

empty_set = set()
set_emp = {}

print(type(empty_set))

set_of_names = {'shiva', "apurva", 'sai', 'kumar','shiva'}
names = {'sai', 'kumar','shiva', 'bhargav', 'lokesh'}
print(set_of_names)

print(len(set_of_names))

set_of_names.add('jain')
print(set_of_names)

lst = ['Shiva', 'Apurva']
name = {'Sai', 'Kumar'}
set_of_names.update(name)
set_of_names.update(lst)
print(set_of_names)

set_of_names.remove('Shiva')
print(set_of_names)

set_of_names.discard('sai')
print(set_of_names)

set_of_names.discard('sai')

set_of_names.pop()
print(set_of_names)

# set_of_names.clear()
# print(set_of_names)

# del(set_of_names)
# print(set_of_names)

lst_set = list(set_of_names)
print(type(lst_set), lst_set)

# union() - update()
# intersection() - common elements
# difference() - removes common elements in the first set you mention

