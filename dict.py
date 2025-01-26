# it has key - value pairs
# mutable datatype
# can use anytype of datatypes in a list
# this will be in a specified order
# key will not accept duplicates
# value will accept duplicates

empty_dict = {}
dict_emp = dict()

print(type(empty_dict))

dict_of_cars = {'maruthi': 'swift',
                'tata':'nexon',
                'hyundai':'creta',
                'audi':'a5',
                'honda':'city'}

print(dict_of_cars)
print(len(dict_of_cars))

print(dict_of_cars['maruthi'])
print(dict_of_cars.get('audi'))
print(dict_of_cars.keys()) # set
print(dict_of_cars.values()) # list
print(dict_of_cars.items()) # both list having tuple

dict_of_cars['honda'] = 'amaze'
print(dict_of_cars)

dict_of_cars.update({'honda' : 'city'})
print(dict_of_cars)

dict_of_cars.pop('honda')
print(dict_of_cars)

# del(dict_of_cars)

dict_of_cars.popitem()
print(dict_of_cars)

dict_of_cars.popitem()
print(dict_of_cars)

dict_of_cars.clear()