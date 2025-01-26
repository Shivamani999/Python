def func_name():
    print("Hello World")

func_name()

def rand(*args):
    print("his name is "+ args[3])

rand('shiva','apurva','jain','koushik')

def names(c2,c1,c3):
    print('youghest child is '+c2)

names(c1='shiva',c2='apurva',c3='jain')

def comb(**kids):
    print('youghest child is '+ kids['c'])

comb(a='siva',b='apurva',c='jain',d='koushik')

def calc(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        if a > b:
            return a - b
        else:
            return b - a
    elif c == '*':
        return a * b
    elif c == '/':
        if a > b:
            return a / b
        else:
            return b / a
    elif c == '**':
        return a ** b

print(calc(2, 4, '**'))

# lambda fn syntax: lambda args : exp
x = lambda a, b: calc(a, b, "**")
print(x(2,4))

