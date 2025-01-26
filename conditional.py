a = "apurva"
send = "Iam {}, from {}"

# if a == "apurva":
#     print("yes this is")
# else:
#     print("someone else is")

#
# num = 10  # even or odd num
# if num % 2 == 0:
#     print("even")
# elif num % 5 == 0:
#     print("divisible by 5")
# else:
#     print("odd")
#
# # nested if condition
# if num % 2 == 0:
#     print("even")
#     if num % 5 == 0:
#         print("divisible by 5")
# else:
#     print("odd")

# write program to find the given number as prime number
number = int(input("Enter a number: "))
if number % 2 == 0 or number % 3 == 0:
    print("not prime")
else:
    print('prime')