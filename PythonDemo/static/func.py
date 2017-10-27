import functools
#可变参数
def multi_param(*params):
    print('可变参数:',params)
    arr_params = []
    for param in params:
        arr_params.append(param)
    print(arr_params)
    return arr_params

multi_param(1, 2, 5, 6)
multi_param([1, 2, 5, 6])
multi_param(*[1, 2, 5, 6])
print('=====================================')

#关键字参数
def volatile_param(name, age, **params):
    print('name:', name, 'age:', age)
    print('关键字参数:', params)

volatile_param('abel', 25, city='SH')
obj = {'city':'SH', 'Tel':123456789}
volatile_param('abel', 25, city='SH', tel=obj['Tel'])
volatile_param('abel', 25, **obj)
print('=====================================')

#命名关键字参数
def named_key_param(name, age, *, city, tel):
    print('name:', name, 'age:', age)
    print('关键字参数:', city, tel)

named_key_param('abel', 25, city='SH', tel=obj['Tel'])
print('=======================================')

#组合参数
def compose_param(a, b, *c, **d):
    print('a=', a, 'b=', b, '*c=', c, '**d=', d)

args = [1, 2, 3]
compose_param(*args, obj)
#compose_param(*args, *obj)  TypeError
compose_param(*args, **obj)

# map调用的函数只能有一个参数==============================
def map_f(x):
    return x*x

print(list(map(map_f, args)))

# reduce调用的函数有两个参数==============================
def reduce_f(x, y):
    return str(x) + str(y)

print(functools.reduce(reduce_f, args))

def str2int(s):
    def char2int(c):
        return {'0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
    # def cal(x, y):

    #     return x*10 + y
    # return functools.reduce(cal, map(char2int, s))
    return functools.reduce(lambda x,y: x*10+y, map(char2int, s))

num = str2int('123456')
print('num is int:', isinstance(num, int))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def sort_L(li):
    return li[0]

print(sorted(L, key=sort_L))